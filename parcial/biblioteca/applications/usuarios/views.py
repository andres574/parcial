from django.shortcuts import render
from .models import Usuario
from django.views.generic import  TemplateView, UpdateView ,ListView, CreateView, DeleteView

class mostrarUsuario(ListView):
    template_name = 'usuarios/mostrarUsuario.html'
    model = Usuario
    context_object_name = 'usuarios'

class addUsuario(CreateView):
    template_name = 'usuarios/addUsuario.html'
    model = Usuario
    fields = ('__all__')
    success_url='.'

class UsuarioActualizar(UpdateView):
    template_name = "usuarios/actualizarUsuario.html"
    model = Usuario
    fields=("__all__")
    success_url='/listarUsuarios/'

class eliminarUsuario(DeleteView):
    template_name = "usuarios/eliminarUsuario.html"
    model= Usuario
    fields=("__all__")
    success_url = '.'