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
    context = {}
    return render(request, "shop_cart.html", context)

def checkout(request):
    context = {}
    return render(request, "checkout.html", context)
