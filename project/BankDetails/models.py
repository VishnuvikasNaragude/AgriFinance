from django.db import models

# Create your models here.
class BankDetails(models.Model):
    bankId = models.IntegerField(primary_key=True)
    bankName = models.CharField(max_length=250)
    accountNumber = models.CharField(max_length=250)
    bankIfsc = models.CharField(max_length=250)
    bankMicr = models.CharField(max_length=250)
    bankAddress = models.CharField(max_length=250)

    def __str__(self):
        return self.bankName