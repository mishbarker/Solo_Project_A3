from django.shortcuts import render

# Create your views here.
def shop_cart(request):
    return render(request, "shop_cart.html")
