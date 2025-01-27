from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('server', 'Server'),
        ('client', 'Client'),
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)

    def is_server(self):
        return self.account_type == 'server'

    def is_client(self):
        return self.account_type == 'client'

class ServerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='server_profile')
    server_specific_field = models.CharField(max_length=255)

class ClientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='client_profile')
    client_specific_field = models.CharField(max_length=255)
