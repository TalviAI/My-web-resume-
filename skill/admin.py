from django.contrib import admin
from skill.models import count,skil



class counts_admin(admin.ModelAdmin):
    list_display=['count_icon','count_numb','count_decs']

class skill_admin(admin.ModelAdmin):
    list_display=['skill','score']


admin.site.register(count,counts_admin)
admin.site.register(skil,skill_admin)
# Register your models here.
