from django.db import models

'''Deberá tener un template, una vista y un modelo (como mínimo, pueden usar más)
La clase del modelo, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)
Se deberán crear como mínimo 3 familiares
Los familiares se deben ver desde la web
'''
class Familiares(models.Model):
    name = models.CharField(max_length=128)
    date_of_birth = models.DateTimeField() 
    height = models.DecimalField(max_digits=5, decimal_places=2)