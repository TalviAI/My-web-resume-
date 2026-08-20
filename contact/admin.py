from django.contrib import admin
from contact.models import contact


class contact_admin(admin.ModelAdmin):
    list_display=['contact_icon','contact_title','contact_desc']



admin.site.register(contact,contact_admin)
# Register your models here.
