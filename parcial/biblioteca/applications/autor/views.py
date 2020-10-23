from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# Create your views here.
from .models import Autores
from django.views.generic import  TemplateView, UpdateView ,ListView, CreateView, DeleteView

class MostrarAutores(ListView):
    c1= Autores.objects.prefetch_related()
    queryset=c1
    fields=('__all__')
    template_name = "autor/listarAutor.html"
    context_object_name = 'autores'


class addAutores(CreateView):
    template_name = 'autor/addAutor.html'
    model = Autores
    fields = ('__all__')
    success_url='.'
class autoresUpdateView(UpdateView):
    template_name = "autor/actualizarAutores.html"
    model = Autores
    fields=("__all__")
    success_url='/listarAutores/'

class eliminarAutores(DeleteView):
    template_name = "eliminarAutor"
    model= Autores
    fields=("__all__")
    success_url = '.'