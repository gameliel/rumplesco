from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .cart import Cart

@login_required
def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s', 'accept_alteration': '%s', 'alteration_price': '%s' }," % (product.id, product.title, product.price, item['quantity'], item['total_price'],  product.get_thumbnail, url, product.num_available, product.accept_alteration, product.alteration_price)

        productsstring = productsstring + b

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        address = request.user.profile.address
        zipcode = request.user.profile.zipcode
        place = request.user.profile.place
        phone = request.user.profile.phone_number
    else:
        first_name = last_name = email = address = zipcode = place = phone = ''

    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'zipcode': zipcode,
        'place': place,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'pub_key_razorpay': settings.RAZORPAY_API_KEY_PUBLISHABLE,
        'pub_key_paypal': settings.PAYPAL_API_KEY_PUBLISHABLE,
        'productsstring': productsstring.rstrip(',')
    }

    return render(request, 'cart.html', context)

def checkout(request):
    return render(request, 'checkout.html')

def success(request):
    cart = Cart(request)
    cart.clear()
    
    return render(request, 'success.html')