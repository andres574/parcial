from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('agregarAutor/', views.addAutores.as_view() ),
    path('listarAutor/', views.MostrarAutores.as_view() ),
    path('actualizarAutor/<pk>/', views.autoresUpdateView.as_view()),

]