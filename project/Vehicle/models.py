from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicalId = models.IntegerField(primary_key=True)
    modelNo = models.CharField(max_length=250)
    Dealer = models.CharField(max_length=250)
    Price = models.CharField(max_length=250)
    onRoadPrice = models.CharField(max_length=250)
    