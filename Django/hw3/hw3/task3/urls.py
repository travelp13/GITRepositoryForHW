from django.urls import path
from .views import *

urlpatterns = [
    path("task3/", custom_file_response, name="custom_file_response"),
]
