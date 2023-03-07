from django.db import models
from .choices import SEX_CHOICES, PACIENTE_CHOICES


class Animal(models.Model):
    id_animal = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    sexo = models.CharField(max_length=15, choices=SEX_CHOICES)
    pais = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    paciente = models.CharField(max_length=100, choices=PACIENTE_CHOICES, blank=True)

    def __str__(self):
        return self.nombre

