from django.db import models

# Create your models here.
class Address(models.Model):
    addressId = models.IntegerField(primary_key=True)
    localHouseNo = models.CharField(max_length=250)
    localArea = models.CharField(max_length=250)
    localLandmark =models.CharField(max_length=250)
    Localcity = models.CharField(max_length=250)
    permanantHouseNo = models.CharField(max_length=250)
    permanantArea = models.CharField(max_length=250)
    permanantLandmark = models.CharField(max_length=250)
    permananatCity = models.CharField(max_length=250)
    Country = models.CharField(max_length=250)

    def __str__(self):
        return self.addressId