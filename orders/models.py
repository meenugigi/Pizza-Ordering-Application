from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from datetime import datetime

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"



class RegularPizza(models.Model):
	name = models.CharField(max_length=64)
	small = models.CharField(max_length=64)
	large = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name} , {self.small} , {self.large}"



class SicilianPizza(models.Model):
	name = models.CharField(max_length=64)
	small = models.CharField(max_length=64)
	large = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.id} - {self.name} , {self.small} , {self.large}"


class Topping(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Subs(models.Model):
	name = models.CharField(max_length=64)
	small = models.CharField(max_length=64)
	large = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name} , {self.small} , {self.large}"


class Pasta(models.Model):
	name = models.CharField(max_length=64)
	price = models.CharField(max_length=64)
	
	def __str__(self):
		return f"{self.name} , {self.price}"


class Salads(models.Model):
	name = models.CharField(max_length=64)
	price = models.CharField(max_length=64)
	
	def __str__(self):
		return f"{self.name} , {self.price}"

class DinnerPlatters(models.Model):
	name = models.CharField(max_length=64)
	small = models.CharField(max_length=64)
	large = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name} , {self.small} , {self.large}"		




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()
    regularpizza = models.ManyToManyField(RegularPizza, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	try:
		instance.profile.save()
	except ObjectDoesNotExist:
		Profile.objects.create(user=instance)





class Orderitem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=64,null=True)
    name=models.CharField(max_length=64)
    cost=models.DecimalField(max_digits=5,decimal_places=2, default=Decimal(0))
    def __str__(self):
    	return f"{self.category} - {self.name} - ${self.cost} "



class Placedorders(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	
	category=models.CharField(max_length=64,null=True)
	name=models.CharField(max_length=64)
	cost=models.DecimalField(max_digits=5,decimal_places=2, default=Decimal(0))
	
	def __str__(self):
		return f"{self.category} - {self.name} - ${self.cost} "


