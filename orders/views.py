from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import RegularPizza, Category, SicilianPizza, Topping, Orderitem, Placedorders, Subs, Pasta, Salads, DinnerPlatters
from django.db.models import Sum
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.conf import settings 
import stripe
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'payment.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        
        return context


@login_required
def index(request):
	context = {
		"c1": Category.objects.first(),
		"regularpizza": RegularPizza.objects.all(),
		"c2": Category.objects.get(id="2"),
		"sicilianpizza": SicilianPizza.objects.all(),
		"c3": Category.objects.get(id="3"),
		"topping": Topping.objects.all(),
		"c4": Category.objects.get(id="4"),
		"subs": Subs.objects.all(),
		"c5": Category.objects.get(id="5"),
		"pasta": Pasta.objects.all(),
		"c6": Category.objects.get(id="6"),
		"salads": Salads.objects.all(),
		"c7": Category.objects.get(id="7"),
		"dinnerplatters": DinnerPlatters.objects.all(),
		"Toppingcost": 0.00,
		"Checkout":Orderitem.objects.filter(user=request.user),
       # "Checkout_category":Orderitem.objects.filter(user=request.user).values_list('category').distinct(),
        "Total":list(Orderitem.objects.filter(user=request.user).aggregate(Sum('cost')).values())[0],
        "user":request.user,
		
	}
	return render(request, "index.html", context)


def login(request):
	return render(request, "registration/login.html")


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request)
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def add(request,category,name,cost):   
    add=Orderitem(user=request.user,category=category,name=name,cost=cost)     
    add.save()  
    add=Placedorders(user=request.user,category=category,name=name,cost=cost)
    add.save()    
    context2 = {
    	"c1": Category.objects.first(),
		"regularpizza": RegularPizza.objects.all(),
		"c2": Category.objects.get(id="2"),
		"sicilianpizza": SicilianPizza.objects.all(),
		"c3": Category.objects.get(id="3"),
		"topping": Topping.objects.all(),
		"c4": Category.objects.get(id="4"),
		"subs": Subs.objects.all(),
		"c5": Category.objects.get(id="5"),
		"pasta": Pasta.objects.all(),
		"c6": Category.objects.get(id="6"),
		"salads": Salads.objects.all(),
		"c7": Category.objects.get(id="7"),
		"dinnerplatters": DinnerPlatters.objects.all(),
		"Toppingcost": 0.00,
        "Checkout":Orderitem.objects.filter(user=request.user),
       # "Checkout_category":Orderitem.objects.filter(user=request.user).values_list('category').distinct(),
        "Total":list(Orderitem.objects.filter(user=request.user).aggregate(Sum('cost')).values())[0],
        "user":request.user,
                     
    }       
    return render(request,"index.html",context2) 



def delete(request,category,name,cost):

	delete=Orderitem.objects.filter(user=request.user,category=category,name=name,cost=cost)[0]
	delete.delete()

	context = {
		"c1": Category.objects.first(),
		"regularpizza": RegularPizza.objects.all(),
		"c2": Category.objects.get(id="2"),
		"sicilianpizza": SicilianPizza.objects.all(),
		"c3": Category.objects.get(id="3"),
		"topping": Topping.objects.all(),
		"c4": Category.objects.get(id="4"),
		"subs": Subs.objects.all(),
		"c5": Category.objects.get(id="5"),
		"pasta": Pasta.objects.all(),
		"c6": Category.objects.get(id="6"),
		"salads": Salads.objects.all(),
		"c7": Category.objects.get(id="7"),
		"dinnerplatters": DinnerPlatters.objects.all(),
		"Toppingcost": 0.00,
		"Checkout":Orderitem.objects.filter(user=request.user),
       # "Checkout_category":Orderitem.objects.filter(user=request.user).values_list('category').distinct(),
        "Total":list(Orderitem.objects.filter(user=request.user).aggregate(Sum('cost')).values())[0],
        "user":request.user
	}
	return render(request,"index.html",context)






def confirmorder(request):
	
	context = {
		"Checkout":Orderitem.objects.filter(user=request.user),
		"Total":list(Orderitem.objects.filter(user=request.user).aggregate(Sum('cost')).values())[0],
		"user":request.user,
		
		"Toppingcost": 0.00,
		
	}
	return render(request, "confirmorder.html", context)



def viewmyorders(request):
	
	context = {
		"Checkout":Placedorders.objects.filter(user=request.user),
		#"Total":list(Orderitem.objects.filter(user=request.user).aggregate(Sum('cost')).values())[0],

		"user":request.user,
		"Toppingcost": 0.00
	}
	return render(request, "viewmyorders.html", context)


