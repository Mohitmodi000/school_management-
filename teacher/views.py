from django.shortcuts import render
from .models import Teacher
# Create your views here.
def teacher_dashboard(request):
    teacher=Teacher.objects.all()
    return render(request, 'teacher.html',{"teachers":teacher})