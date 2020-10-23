from django.db import models
from applications.libro.models import Libro 
from applications.usuarios.models import Usuario

# Create your models here.
class Prestamo(models.Model):
    idPrestamo = models.IntegerField(primary_key = True)
    idlibro = models.ForeignKey(Libro, on_delete = models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    fechaPrestamo = models.DateTimeField()
    fechaDevolucion = models.DateTimeField()


    def _str_(self):
        return self.idPrestamo