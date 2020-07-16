from django.shortcuts import render

# Create your views here.
def show_one(request):
    context = {}
    return render(request, "show_one.html", context)