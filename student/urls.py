from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.all_students, name="students")
]