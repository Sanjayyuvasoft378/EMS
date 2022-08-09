from django.db import models

# Create your models here.
class Employee(models.Model):
    fullName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phoneNo = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=20)

