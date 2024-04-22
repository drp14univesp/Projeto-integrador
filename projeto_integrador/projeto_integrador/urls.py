
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuario_view, name='listagem_usuarios'),
    path('exibir_usuarios/', views.exibir_usuarios, name='exibir_usuarios'),
    path('usuario/delete/<int:id_usuario>/', views.delete_usuario, name='delete_usuario'),
    path('usuario/atualizar/<int:id_usuario>/', views.atualizar_usuario, name='atualizar_usuario'),
]


