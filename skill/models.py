from django.db import models


class count(models.Model):
    count_icon=models.CharField(max_length=50,blank=True)
    count_numb=models.IntegerField(blank=True)
    count_decs=models.CharField(max_length=25,blank=True)

class skil(models.Model):
    skill=models.CharField(max_length=25,blank=True)
    score=models.IntegerField(blank=True)

# Create your models here.
