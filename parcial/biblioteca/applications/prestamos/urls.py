from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('agregarPrestamo/', views.addPrestamo.as_view() ),
    path('listarPrestamo/', views.mostrarPrestamo.as_view() ),
    path('actualizarPrestamo/<pk>/', views.PrestamoUpdateView.as_view()),
     path('eliminarPrestamo/<pk>/', views.eliminarPrestamo.as_view()),


]