from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, Cart, User, Pizza, Topping,PromoCode, Review, Order, Address, Category
# Create your views here.


#menu template  
# menus = [
#     {'id': 2422, 'name': 'Veggie'}, 
#     {'id': 2222, 'name': 'Vggie'}, 
#     {'id': 2322, 'name': 'Vegie'}, 
#     {'id': 2522, 'name': 'Vgie'}, 
#     {'id': 2622, 'name': 'Veie'}, 
#     {'id': 2722, 'name': 'Vegge'}, 
#     {'id': 2822, 'name': 'Veggi'}, 
#     {'id': 2922, 'name': 'egge'}, 
#     {'id': 2122, 'name': 'egi'}, 
    
# ]

def home(request):
    menus = Menu.objects.all()
    context = {'menus': menus}
    return render(request, 'blog/home.html', context)

def menu(request, pk):
    menu = Menu.objects.get(id=pk)
    context = {'menu': menu}
    return render(request, 'blog/menu.html', context)


#def user_detail(request, user_id):
 #   user = User.objects.get(id=user_id)
  #  return render(request, 'user_detail.html', {'user': user})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = Address(request.POST)
        if form.is_valid():
            # Save the address
            address = form.cleaned_data['delivery_address']
            user.delivery_address = address
            user.save()
            # Redirect or add success message

    else:
        form = Address(initial={'delivery_address': user.delivery_address})

    context = {'user': user, 'form': form}
    return render(request, 'user_detail.html', context)

def pizza_detail(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    return render(request, 'pizza_detail.html', {'pizza': pizza})

def add_to_cart(request, pizza_id):
    # Retrieve the pizza object based on the provided pizza_id
    pizza = Pizza.objects.get(pk=pizza_id)

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get the user's cart or create a new one if it doesn't exist
        cart, created = Cart.objects.get_or_create(user=request.user, pizza=pizza)

        # Increment the quantity if the pizza is already in the cart
        if not created:
            cart.quantity += 1
            cart.save()

        # Redirect the user to the cart page or any other desired page
        return redirect('cart')
    else:
        # Handle the case for anonymous/guest users
        # You can implement different logic based on your requirements
        # For example, you can use session variables to store the cart items
        return redirect('login')  # Redirect to the login page

def view_cart(request):
    # Retrieve all cart items for the current user
    cart_items = Cart.objects.all()
    if request.user.is_authenticated:
        # Retrieve cart items for the logged-in user
        cart_items = Cart.objects.filter(user_id=request.user.id)
    else:
        # Retrieve cart items for the guest user (using session-based approach)
        cart_items = Cart.objects.filter(session_id=request.session.session_key)

    context = {
        'cart_items': cart_items
    }

    return render(request, 'blog/cart.html', context)


def topping_detail(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    return render(request, 'topping_detail.html', {'topping': topping})

def promo_code_detail(request, promo_code_id):
    promo_code = PromoCode.objects.get(id=promo_code_id)
    return render(request, 'promo_code_detail.html', {'promo_code': promo_code})

def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', {'review': review})

def order_item_detail(request, order_item_id):
    order_item = Order.objects.get(id=order_item_id)
    return render(request, 'order_item_detail.html', {'order_item': order_item})

