from django.db import models

# Create your models here.
class Guaranter(models.Model):
    guaranterId = models.IntegerField(primary_key=True)
    guranterName = models.CharField(max_length=250)
    guaranterAddress = models.CharField(max_length=250)
    guaranterRealtionshipwithcustomer = models.CharField(max_length=250)
    guaranterMobileNo = models.CharField(max_length=250)
    aadharCardNo = models.CharField(max_length=250)
    jobDetails = models.CharField(max_length=250)

    def __str__(self):
        return self.guranterName