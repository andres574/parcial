from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('agregarUsuario/', views.addUsuario.as_view() ),
    path('listarUsuario/', views.mostrarUsuario.as_view() ),
    path('actualizarUsuario/<pk>/', views.UsuarioActualizar.as_view()),

]