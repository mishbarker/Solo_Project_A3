from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "index.html", context)

def show_one(request):
    context = {}
    return render(request, "show_one.html", context)

def shop_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {
        'items':items,
        'order':order,
    }
    return render(request, "shop_cart.html", context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {
        'items':items,
        'order':order,
    }
    return render(request, "checkout.html", context)
