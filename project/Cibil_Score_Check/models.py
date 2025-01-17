from django.db import models

# Create your models here.
class CibilScoreCheck(models.Model):
    cibilId = models.IntegerField(primary_key= True)
    customerPanNo = models.IntegerField()
    Score = models.IntegerField()
    Cibil_status = models.CharField(max_length=250)
    Remark = models.CharField(max_length=25)

    def __str__(self):
        return self.customerPanNo


 