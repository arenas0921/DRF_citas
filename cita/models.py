from django.db import models


# Create your models here.
class Cita(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now=True)