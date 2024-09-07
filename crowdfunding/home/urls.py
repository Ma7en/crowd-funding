from django.urls import path
from .views import index

uurlpatterns = [
    path("", index, name="index"),
]
