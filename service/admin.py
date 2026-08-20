from django.contrib import admin
from service.models import service


class service_admin(admin.ModelAdmin):
    list_display=['service_icon','service_title','service_desc']

admin.site.register(service, service_admin)


# Register your models here.
