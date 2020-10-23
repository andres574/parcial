from django.shortcuts import render
from .models import Prestamo
from django.views.generic import  TemplateView, UpdateView ,ListView, CreateView, DeleteView


# Create your views here.
class mostrarPrestamo(ListView):
    c1= Prestamo.objects.prefetch_related()
    queryset=c1
    fields=('__all__')
    template_name = "prestamo/mostrarPrestamo.html"
    context_object_name = 'listarPrestamo'

class addPrestamo(CreateView):
    template_name = 'prestamo/addPrestamo.html'
    model = Prestamo
    fields = ('__all__')
    success_url='.'

class PrestamoUpdateView(UpdateView):
    template_name = "prestamo/actualizarPrestamo.html"
    model = Prestamo
    fields=("__all__")
    success_url='.'

class eliminarPrestamo(DeleteView):
    template_name = "eliminarPrestamo.html"
    model= Prestamo
    fields=("__all__")
    success_url = '.'