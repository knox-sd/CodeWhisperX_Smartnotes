from django.urls import path

from . import views

urlpatterns = [
    # path('home', views.home),
    # path('authorized', views.authorized),
    
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthoriizdView.as_view),

]
