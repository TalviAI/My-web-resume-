from django.db import models
class service(models.Model):
    service_icon=models.CharField(max_length=50,blank=True)
    service_title=models.CharField(max_length=50,blank=True)
    service_desc=models.TextField(blank=True)


# Create your models here.