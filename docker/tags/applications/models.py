from django.db import models


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    owner = models.CharField(max_length=250)
