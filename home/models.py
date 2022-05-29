from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    phone = models.CharField(max_length=10, null=True)
    desc = models.TextField(null=True)
    date = models.DateField(null=True)
