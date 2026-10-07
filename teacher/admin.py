from django.contrib import admin
from .models import Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth', 'hire_date', 'subject')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('subject', 'class_assigned')
