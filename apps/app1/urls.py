from django.urls import path, include
from .import views

urlpatterns = [

    path('', views.index), #GET renders home.html for shopping homepage
    path('show_one/', views.show_one), #will need <int:id> added back in
    path('shop_cart/', views.shop_cart), #will need <int:id> added back in

    # path('submit_review/<int:id>', views.submit_review), #POST that redirects to /show_one_book/<int:id>
    # path('delete_review/<int:id>', views.delete_review), #POST/GET redirects to same page /show_one_book/<int:id>
    # path('user_profile/<int:id>', views.user_profile), #renders profile.html with redirects to /show_one_book/<int:id> OR HOME OR /new OR /logout
    
]