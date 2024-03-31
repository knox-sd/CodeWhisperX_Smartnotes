from django.urls import path

from . import views

urlpatterns = [
    # path('home', views.HomeView.as_view(), name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthoriizdView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),


    # path('home', views.home),
    # path('authorized', views.authorized),
]
