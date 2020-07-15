from django.urls import path
from .import views

urlpatterns = [

    path('', views.show_one), #will need <int:id> added back in
    
]