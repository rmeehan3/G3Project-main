from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



#starting with the models. 


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    delivery_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.user.username
    # ...

#menu for specified item 
class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated_model  = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name 
    
class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
   
    # ...

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    guest_email = models.EmailField(blank=True, null=True)
    pizza = models.ManyToManyField(Pizza)
    order_id = models.IntegerField()
    order_type = models.CharField(max_length=10090)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


    def __str__(self) -> str:
        return f"Order #{self.pk } - Customer: {self.customer.username if self.customer else 'Guest'}"
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 rating scale
    comment = models.TextField()
    # ...

class Topping(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # ...

class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    # ...

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Add additional fields as needed

    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    # Add additional fields as needed

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zipcode}"