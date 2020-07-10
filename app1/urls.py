from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index), #GET renders index.html for register or login
   
   
    path('register', views.register), #POST redirect to index or redirect to /all_reviews
    path('login', views.login), #POST redirect to index or redirect to /all_reviews
    path('logout', views.logout),
    path('all_reviews', views.all_reviews), #GET renders all_reviews.html - HOME
    path('new', views.new), #GET renders to add a new book and review
    path('create', views.create), #POST adds a new book,review, rating, may add new author and redirects to show_one_book/<int:id>
    path('show_one_book/<int:id>', views.show_one_book),
    path('submit_review/<int:id>', views.submit_review), #POST that redirects to /show_one_book/<int:id>
    path('delete_review/<int:id>', views.delete_review), #POST/GET redirects to same page /show_one_book/<int:id>
    path('user_profile/<int:id>', views.user_profile), #renders profile.html with redirects to /show_one_book/<int:id> OR HOME OR /new OR /logout
    
]