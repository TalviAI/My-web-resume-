from django.db import models


class contact(models.Model):
    contact_icon=models.CharField(max_length=50,blank=True)
    contact_title=models.CharField(max_length=50,blank=True)
    contact_desc=models.CharField(max_length=100,blank=True)

# Create your models here.
