from audioop import maxpp
import numbers
from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.

class Webpage(models.Model):
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class Topico(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    topic = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return str(self.topic)

class Pagina (models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number)