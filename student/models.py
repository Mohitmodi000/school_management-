from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)
    class_name = models.PositiveIntegerField(default=1)  # Assuming class is represented by a number

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
