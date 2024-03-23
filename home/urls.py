from django.urls import path

from . import views

urlpatterns = [
    # path('home', views.home),
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthoriizdView.as_view),
    # path('authorized', views.authorized),
]
