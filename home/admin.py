from django.contrib import admin
from home.models import home,socialmedia


class home_admin(admin.ModelAdmin):
    list_display=['home_logo','home_name','home_desc','home_skill','home_loction']


class social_media(admin.ModelAdmin):
    list_display1=['social_plateform','social_url']

admin.site.register(home, home_admin)
admin.site.register(socialmedia,social_media)

# Register your models here.
