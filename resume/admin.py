from django.contrib import admin
from resume.models import Education,Experience,summary


class education_admin(admin.ModelAdmin):
    list_display=['Degree','startdate','enddate','univercity','acitvies']


class Experience_admin(admin.ModelAdmin):
    list_display=['desination','startdate','enddate','companyname','description']

class summary_admin(admin.ModelAdmin):
    list_display=['summary']


admin.site.register(Education,education_admin)
admin.site.register(Experience,Experience_admin)
admin.site.register(summary,summary_admin)
# Register your models here.
