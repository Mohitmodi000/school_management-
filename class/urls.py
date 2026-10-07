from django.urls import path
from . import views

urlpatterns = [
    path("class/", views.all_classes, name="classes"),
    ]