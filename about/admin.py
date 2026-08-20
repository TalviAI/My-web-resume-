from django.contrib import admin
from about.models import about,informati

class abouts_admin(admin.ModelAdmin):
    list_display=['heading','abouts']

class info_admin(admin.ModelAdmin):
    list_display1=['field_name','detail_name']


    




admin.site.register(about,abouts_admin)
admin.site.register(informati,info_admin)


# Register your models here.
