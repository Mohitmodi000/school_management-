from django.db import models

# Create your models here.
class Teacher(models.Model):
     GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")]
     
     SUBJECT_CHOICES= [
        ("Math", "Mathematics"),   
        ("Sci", "Science"),
        ("Eng", "English"),
        ("Hist", "History"),
        ("Geo", "Geography"),
        ("Art", "Art"),
        ("PE", "Physical Education"),
        ("Music", "Music"),
        ("Comp", "Computer Science"),
        ("Lang", "Foreign Language"),
        ("Econ", "Economics"),
        ("Poli", "Political Science"),
        ("Psych", "Psychology"),
        ("Soc", "Sociology"),
        ("Phil", "Philosophy"),
        ("Rel", "Religious Studies"),
        ("Bus", "Business Studies"),
        ("Law", "Law"),
        ("Med", "Medical Studies"),
        ("EngLit", "English Literature"),
        ("HistArt", "History of Art"),
        ("Anthro", "Anthropology"),
        ("Arch", "Architecture"),
        ("EnvSci", "Environmental Science"),
     ]
     CLASS_CHOICES = [
        (1, "Class 1"),
        (2, "Class 2"),
        (3, "Class 3"),
        (4, "Class 4"),
        (5, "Class 5"),
        (6, "Class 6"),
        (7, "Class 7"),
        (8, "Class 8"),
        (9, "Class 9"),
        (10, "Class 10"),
        (11, "Class 11"),
        (12, "Class 12"),
     ]
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     email = models.EmailField(unique=True)
     date_of_birth = models.DateField()
     hire_date = models.DateField(auto_now_add=True)
     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  # Assuming gender is represented by a single character
     subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)  # Assuming subject is represented by a string
     class_assigned = models.IntegerField(choices=CLASS_CHOICES)  # Assuming class is represented by an integer

     def __str__(self):
        return f"{self.first_name} {self.last_name}"