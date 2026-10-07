from django.shortcuts import render
from .models import Student

# Create your views here.
def all_students(request):
    # Logic to retrieve all students from the database
    students = Student.objects.all()  # Assuming you have a Student model
    return render(request, 'all_student.html', {'students': students})