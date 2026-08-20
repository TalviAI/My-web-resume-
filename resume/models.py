from django.db import models


class Education(models.Model):
    Degree=models.CharField(max_length=50,blank=True)
    startdate=models.DateField(auto_now=False, auto_now_add=False,blank=True)
    enddate=models.DateField(auto_now=False, auto_now_add=False,blank=True)
    univercity=models.CharField(max_length=250,blank=True)
    acitvies=models.TextField(blank=True)


class Experience(models.Model):
    desination=models.CharField(max_length=50,blank=True)
    startdate=models.DateField(auto_now=False, auto_now_add=False,blank=True)
    enddate=models.DateField(auto_now=False, auto_now_add=False,blank=True)
    companyname=models.CharField(max_length=200,blank=True)
    description=models.TextField(blank=True)

class summary(models.Model):
    summary=models.TextField(blank=True)
# Create your models here.
