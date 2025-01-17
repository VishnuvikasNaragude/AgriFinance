from django.db import models

# Create your models here.
class Enquiry(models.Model):
    STATUS =(('Single','Single'),('Married','Married'))
    enq_id = models.IntegerField(primary_key=True)
    enq_name = models.CharField(max_length=120)
    enqpancardno =models.CharField(max_length=240)
    enq_mobileno = models.CharField(max_length=11)
    enq_age = models.IntegerField()
    enq_status = models.CharField(max_length=250)
    enq_email = models.EmailField()
    enq_vehicle_name = models.CharField(max_length=250,choices=STATUS)

    def __str__(self):
        return self.enq_name