from django.urls import path, include
from .import views

urlpatterns = [

    path('', views.index, name="store"),
    path('show_one/<int:id>', views.show_one, name="show_one"), 
    path('shop_cart/', views.shop_cart, name="shop_cart"), 
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    
    
]