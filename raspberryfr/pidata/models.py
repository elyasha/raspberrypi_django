from django.db import models

# Create your models here.

class Medida1(models.Model):
    tensao_eletrica = models.FloatField()

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} Volts".format(self.tensao_eletrica)
