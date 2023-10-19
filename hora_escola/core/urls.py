from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro', views.sign_up, name="sign_up"),
    
]
