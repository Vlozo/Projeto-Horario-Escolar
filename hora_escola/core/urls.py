from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.sign_in, name="sign_in"),
    path('cadastro', views.sign_up, name="sign_up"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home', views.home, name="home"),
]

