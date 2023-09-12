from django.db import models

# Create your models here.

class Trabajo(models.Model):
    
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.numero}'
    
class Trabajador(models.Model):
     
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Entregas(models.Model):
     
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)
