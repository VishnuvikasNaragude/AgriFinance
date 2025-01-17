from django.db import models
from Vehicle.models import Vehicle

class Customer(models.Model):
    customerId = models.IntegerField(primary_key=True)
    customerName = models.CharField(max_length=250)
    customerMobileno = models.IntegerField()
    customerLoanAmount = models.IntegerField()
    customerAge = models.IntegerField()
    customerDateofBirth = models.CharField(max_length=252)
    customerEmail = models.EmailField()
    customerPancardno = models.CharField(max_length=250)
    Address = models.TextField(max_length=300)
    vehicalId = models.ForeignKey(Vehicle,on_delete=models.CASCADE, null=True, blank=True)
    Bank = models.CharField(max_length=220)
    Guaranter = models.CharField(max_length=250)
    loandetails = models.CharField(max_length=250)

    def __str__(self):
        return self.customerName


