from django.shortcuts import render
from .models import Libro

# Create your views here.
from django.views.generic import  TemplateView, UpdateView ,ListView, CreateView, DeleteView



class mostrarLibros(ListView):
    template_name = 'libro/libros.html'
    model = Libro
    context_object_name = 'listar'

class addLibro(CreateView):
    template_name = 'libro/addLibro.html'
    model = Libro
    fields = ('__all__')
    success_url='.'

class libroUpdateView(UpdateView):
    template_name = "libro/actualizarLibro.html"
    model = Libro
    fields=("__all__")
    success_url='/listarLibro/'

class eliminarLibro(DeleteView):
    template_name = "libro/eliminarLibro.html"
    model= Libro
    fields=("__all__")
    success_url = '.'

class vistaHome(TemplateView):
    template_name = "libro/home.html"