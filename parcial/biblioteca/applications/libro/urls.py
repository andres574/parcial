from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('listarLibros/', views.mostrarLibros.as_view() ),
    path('agregarLibro/', views.addLibro.as_view() ),
    path('actualizarLibro/<pk>/', views.libroUpdateView.as_view()),
    path('eliminarLibro/<pk>/', views.eliminarLibro.as_view()),
    path('home/', views.vistaHome.as_view()),
]