from django.urls import path
from .import views

urlpatterns = [

    path('', views.shop_cart), #will need <int:id> added back in
    
]