from django.contrib import admin
from .models import Menu, Pizza, Topping, User, Order, PromoCode, Review

admin.site.register(Menu)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(PromoCode)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Pizza)


