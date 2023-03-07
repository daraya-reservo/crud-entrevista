from django.db import models

# Create your models here.
class Animal(models.Model):
    id_animal = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    sexo = models.CharField(max_length=15)
    pais = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    paciente = models.CharField(max_length=100)

