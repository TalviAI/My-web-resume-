from django.db import models

class about(models.Model):
    heading=models.CharField(max_length=50,blank=True)
    abouts=models.TextField(blank=True)

class informati(models.Model):
    field_name=models.CharField(max_length=50,blank=True)
    detail_name=models.CharField(max_length=50,blank=True)


# Create your models here.
