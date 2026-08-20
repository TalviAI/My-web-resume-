from django.contrib import admin
from form.models import form

class form_admin(admin.ModelAdmin):
    list_display=['name','email','subject','message']

admin.site.register(form,form_admin)
# Register your models here.
