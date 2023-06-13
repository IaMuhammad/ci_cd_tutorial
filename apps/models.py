from django.db import models


# Create your models here.
class AModel(models.Model):
    name = models.CharField(max_length=255)
