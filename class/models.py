from django.db import models
from teacher.models import Teacher

# Create your models here.
class classes(models.Model):
    class_name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    class_schedule = models.TextField()

    def __str__(self):
        return self.class_name
