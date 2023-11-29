from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name = "menu"), 
    path('menu/<int:pk>/', views.menu_item, name='menu'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('pizzas/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('toppings/<int:topping_id>/', views.topping_detail, name='topping_detail'),
    path('order-items/<int:order_item_id>/', views.order_item_detail, name='order_item_detail'),
    path('cart/add/<int:pizza_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('promo-codes/<int:promo_code_id>/', views.promo_code_detail, name='promo_code_detail'),
    path('register/', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


