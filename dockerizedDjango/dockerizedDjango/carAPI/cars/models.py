from django.db import models


# Create your models here.

class Cars(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20, unique=True)
