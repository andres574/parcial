from django.db import models

# Create your models here.
class Libro(models.Model):
    idLibro = models.IntegerField(primary_key = True)
    codigo = models.IntegerField()
    titulo = models.CharField(max_length = 100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    numPags = models.IntegerField()


    def _str_(self):
        return self.idLibro