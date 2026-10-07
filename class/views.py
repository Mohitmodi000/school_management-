from django.shortcuts import render
from .models import classes
# Create your views here.

def all_classes(request):
    # Logic to retrieve all classes from the database
    classs = classes.objects.all()  # Assuming you have a Class model
    return render(request, 'classes.html', {'classes': classs})