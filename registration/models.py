# registration/models.py
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    reason = models.TextField()

    def __str__(self):
        return self.name
