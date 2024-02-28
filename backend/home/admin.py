from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.FacultyDetail)
class FacultyDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'email', 'city', 'state', 'photo']



