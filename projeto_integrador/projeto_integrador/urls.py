
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuario/', views.usuario_view, name='listagem_usuarios'),
    path('exibir_usuarios/', views.exibir_usuarios, name='exibir_usuarios'),
]
