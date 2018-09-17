from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {})


def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id) # grab the object
    cart_obj, new_obj = Cart.objects.new_or_get(request) # grab the cart or create one
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj) # cart_obj.products.add(product_id) - add to m2m
    # cart_obj.products.remove(obj) - remove from m2m
    return redirect('cart:home')
