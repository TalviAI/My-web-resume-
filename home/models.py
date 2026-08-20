from django.db import models


class home(models.Model):
    home_logo=models.ImageField((""), upload_to="static/img", height_field=None, width_field=None, max_length=None ,blank=True)
    home_name=models.CharField(max_length=50,blank=True)
    home_desc=models.TextField(blank=True)
    home_skill=models.CharField(max_length=100,blank=True)
    home_loction=models.CharField(max_length=100,blank=True)

class socialmedia(models.Model):
    social_plateform=models.CharField(max_length=50,blank=True)
    social_url=models.URLField(max_length=250,blank=True)

# Create your models here.
