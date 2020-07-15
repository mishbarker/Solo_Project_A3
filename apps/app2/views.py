from django.shortcuts import render

# Create your views here.
def show_one(request):
    return render(request, "show_one.html")