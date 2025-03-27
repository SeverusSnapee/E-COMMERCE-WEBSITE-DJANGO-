from django.shortcuts import render, redirect
from .models import Product
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from decimal import Decimal
from .models import Order, OrderItem, Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.db.models import Count
def cart_view(request):
    cart = request.session.get('cart', {})
    total = Decimal('0.00')  # Initialize total as a Decimal object

    # Loop through the cart to calculate item totals and the overall total
    for item in cart.values():
        item['total_price'] = item['price'] * item['quantity']
        total += item['total_price']

    return render(request, 'cart.html', {'cart': cart, 'total': total})

def landing_page(request):
     featured_products = Product.objects.all()[:3]  # Fetch latest 3 products

     return render(request, 'index.html', {'featured_products': featured_products})

def product_listing(request):
    query = request.GET.get('search', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'products.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle the image upload with request.FILES
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('product_listing')  # Redirect to the product listing page after saving
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def product_detail(request, id):
    # Get the product by id, or 404 if not found
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
def product_listing(request):
    # Get the search query from the GET request
    search_query = request.GET.get('search', '')

    if search_query:
        # Filter the products by the search query (case-insensitive search)
        products = Product.objects.filter(name__icontains=search_query)
    else:
        # If there's no search query, show all products
        products = Product.objects.all()

    return render(request, 'product_listing.html', {'products': products, 'search_query': search_query})
# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart = request.session.get('cart', {})

#     # Convert the price to float before storing it in the session
#     product_price = float(product.price)

#     # If the product is already in the cart, update the quantity
#     if str(product.id) in cart:
#         cart[str(product.id)]['quantity'] += 1
#     else:
#         cart[str(product.id)] = {
#             'name': product.name,
#             'price': product_price,  # Store as float
#             'quantity': 1,
#             'image': product.image.url
#         }

#     # Save the updated cart to the session
#     request.session['cart'] = cart

#     return redirect('cart')  # Redirect to the cart page


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})

    # Convert the price to float before storing it in the session
    product_price = float(product.price)

    # If the product is already in the cart, update the quantity
    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {
            'id': product.id,          # Add the id to the cart item
            'name': product.name,
            'price': product_price,    # Store as float
            'quantity': 1,
            'image': product.image.url
        }

    # Debugging print to check cart contents
    print("Cart after adding product:", cart)

    # Save the updated cart to the session
    request.session['cart'] = cart

    return redirect('cart')  # Redirect to the cart page

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    # Remove the product from the cart if it exists
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart

    return redirect('cart')  # Redirect back to the cart page

def cart(request):
    cart = request.session.get('cart', {})
    total_price = 0

    # Loop through the cart to calculate item totals and the overall total
    for item_id, item in cart.items():
        # Calculate total price per product (price * quantity)
        item_total_price = float(item['price']) * item['quantity']
        item['total_price'] = item_total_price  # Add total_price to each item in the cart
        total_price += item_total_price  # Add to the overall total price

    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})
 
# def checkout(request):
#     cart = request.session.get('cart', {})
#     total_price = 0
#     total_price_product={}

#     # Debugging print to check cart contents in the checkout view
#     print("Cart during checkout:", cart)

#     # Create the order if there's a valid cart
#     if cart:
#         # Create the order without the total_price field
#         order = Order.objects.create(user=request.user)

#         # Loop through the cart to create OrderItem objects and calculate the total
#         for item in cart.values():
#             if 'id' not in item:
#                 print("Missing 'id' in cart item:", item)
#                 continue  # Skip items without an 'id'

#             product = Product.objects.get(id=item['id'])  # Accessing 'id' from the cart item
#             total_price += item['price'] * item['quantity']
#             total_price_product = item['price'] * item['quantity']

#             # Create an OrderItem for each item in the cart
#             OrderItem.objects.create(
#                 order=order,
#                 product=product,
#                 quantity=item['quantity']
#             )

#         # Optionally, clear the cart after creating the order
#         request.session['cart'] = {}

#         # Redirect to the order confirmation page
#         # return redirect('order_confirmation', order_id=order.id)
#         return render(request, 'order_confirmation.html', {'cart': cart, 'total_price': total_price, 'total_price_product': total_price_product})
# def checkout(request):
#     user = request.user
#     cart = request.session.get('cart', {})

#     if not cart:
#         messages.error(request, "Your cart is empty!")
#         return redirect("cart")

#     order = Order.objects.create(user=user, ordered=True)

#     for product_id, item in cart.items():
#         product = get_object_or_404(Product, id=product_id)
#         order_item = OrderItem.objects.create(
#             order=order,  # Link OrderItem to Order
#             product=product,
#             quantity=item['quantity']
#         )
    
#     # Clear cart after saving order
#     request.session['cart'] = {}

#     return redirect("order_confirmation", order_id=order.id)
def checkout(request):
    user = request.user
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect("cart")

    order = Order.objects.create(user=user, ordered=True)

    for product_id, item in cart.items():
        product = get_object_or_404(Product, id=product_id)
        OrderItem.objects.create(
            order=order,  
            product=product,
            quantity=item['quantity']
        )
    
    # Clear cart after saving order
    request.session['cart'] = {}

    return redirect("order_confirmation", order_id=order.id)

   
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log in the user after registration
#             return redirect("home")  # Redirect to homepage or products page
#     else:
#         form = UserCreationForm()
#     return render(request, "register.html", {"form": form})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')  # Redirect to login page after registration
        else:
            messages.error(request, 'There was an error in the registration form')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
def popular_products(request):
    
    popular_products = OrderItem.objects.values('product__id', 'product__name') \
                                        .annotate(total_purchases=Count('product')) \
                                        .order_by('-total_purchases')[:10]
    
    
    popular_products = [
        {'product': Product.objects.get(id=item['product__id']), 'total_purchases': item['total_purchases']}
        for item in popular_products
    ]
    
    return render(request, 'popular_products.html', {'popular_products': popular_products})