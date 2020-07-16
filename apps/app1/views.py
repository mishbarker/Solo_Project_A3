from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)

def show_one(request):
    context = {}
    return render(request, "show_one.html", context)

def shop_cart(request):
    context = {}
    return render(request, "shop_cart.html", context)
