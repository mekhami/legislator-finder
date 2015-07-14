from django.db import models

# Create your models here.
class Legislator(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()

