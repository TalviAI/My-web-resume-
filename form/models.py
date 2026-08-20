from django.db import models

class form(models.Model):
    name=models.CharField(max_length=50,blank=True)
    email=models.EmailField(blank=True)
    subject=models.CharField(max_length=75,blank=True)
    message=models.TextField(blank=True)

# Create your models here.
