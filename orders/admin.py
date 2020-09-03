from django.contrib import admin
from .models import RegularPizza, SicilianPizza, Category, Topping, Orderitem, Placedorders,Subs, Pasta, Salads, DinnerPlatters
# Register your models here.

# Register your models here.
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Topping)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(Category)
admin.site.register(Orderitem)
admin.site.register(Placedorders)
