from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/<str:pk>/', views.menu, name = "menu"), 
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('pizzas/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('toppings/<int:topping_id>/', views.topping_detail, name='topping_detail'),
    path('order-items/<int:order_item_id>/', views.order_item_detail, name='order_item_detail'),
    path('reviews/<int:review_id>/', views.review_detail, name='review_detail'),
    path('promo-codes/<int:promo_code_id>/', views.promo_code_detail, name='promo_code_detail'),
]


