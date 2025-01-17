from django.db import models

# Create your models here.
class PreviousLoan(models.Model):
    previousloanId = models.IntegerField(primary_key=True)
    previousLoanamount = models.CharField(max_length=250)
    previousLoanStatus = models.CharField(max_length=250)
    Tenure = models.CharField(max_length=250)
    paidAmount = models.CharField(max_length=250)
    remainingAmount = models.CharField(max_length=250)
    bank = models.CharField(max_length=250)

    def __str__(self):
        return self.previousloanId