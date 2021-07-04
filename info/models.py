from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mob=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table='register'