from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('processar_formulario/', views.processar_formulario, name="processar_formulario")
    
]
