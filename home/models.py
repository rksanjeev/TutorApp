from venv import create
from django.db import models

# Create your models here.

class LeadModel(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(unique=True)
    subject = models.TextField(max_length=255, null=False)
    message = models.TextField(max_length=255, blank=False, null=False)
    phone = models.BigIntegerField(blank=False, null=True)
    date = models.DateField(auto_now_add=True)

    def save(self) -> None:
        return super().save()


