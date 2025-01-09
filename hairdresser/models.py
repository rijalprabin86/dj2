from django.db import models

# Create your models here.
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

class Hairdresser(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Appointment(models.Model):
    date = models.DateTimeField()
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    notes = models.TextField(blank=True)