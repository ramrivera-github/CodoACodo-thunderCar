from django.db import models

# Create your models here.
class solenoide(models.Model):
    apellido = models.CharField(max_length=200)
    nombre = models.CharField(max_length=30)
    dni = models.IntegerField()
    fecNac = models.DateField()
    email = models.EmailField(max_length=100)
    adjuntar = models.FileField()
    consulta = models.TextField(max_length=250)

class Contacto(models.Model):
    apellido = models.CharField(max_length=200)
    nombre = models.CharField(max_length=30)
    dni = models.IntegerField()
    fecNac = models.DateField()
    email = models.EmailField(max_length=100)
    adjuntar = models.FileField(upload_to='contactos/')
    consulta = models.TextField(max_length=250)