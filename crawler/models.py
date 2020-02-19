from django.db import models

# Create your models here.
class Veiculos(models.Model):

    modelo = models.CharField(max_length=100)

    def __str__(self):
        return self.modelos