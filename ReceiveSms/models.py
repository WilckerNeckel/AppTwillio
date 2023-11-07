from django.db import models

class SmsInfo(models.Model):
    message = models.CharField(max_length=50)
    sender = models.CharField(max_length=20)
    recipient = models.CharField(max_length=20)
   
    def __str__(self):
        return self.sender
