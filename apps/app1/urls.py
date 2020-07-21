from django.urls import path, include
from .import views

urlpatterns = [

    path('', views.index, name="store"), #GET renders index.html for shopping homepage
    path('show_one/<int:id>', views.show_one, name="show_one"), #will need <int:id> added back in
    path('shop_cart/', views.shop_cart, name="shop_cart"), #will need <int:id> added back in
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    
    
]