from django.db import models

# Create your models here.
class DocumentDetails(models.Model):
    documentId = models.IntegerField(primary_key=True)
    customerId = models.IntegerField()
    Pancard = models.FileField(upload_to='documents/')
    Aadharcard = models.FileField(upload_to='documents/')
    Phote = models.FileField(upload_to='documents/')
    Signature = models.FileField(upload_to='documents/')
    Postdatedcheque = models.FileField(upload_to='documents/')
    Thumb = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.customerId