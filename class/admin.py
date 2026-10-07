from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import classes
# Register your models here.
@admin.register(classes)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'class_teacher', 'class_schedule']
    list_filter = ['class_teacher']
    search_fields = ['class_name', 'class_teacher']

