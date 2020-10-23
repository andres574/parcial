from django.db import models

# Create your models here.


from applications.libro.models import Libro


class Autores(models.Model):
    idAutor= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    idlibro = models.ForeignKey(Libro, on_delete = models.CASCADE)


    def str(self):
        return self.idAutor
