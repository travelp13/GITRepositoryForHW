from django.urls import path
from .views import *

urlpatterns = [
    path("task4/", home_view, name="task4_home"),
    path("task4/text_response/", text_response, name="text_response"),
    path("task4/html_response/", html_response, name="html_response"),
    path("task4/json_response/", json_response, name="json_response"),
    path("task4/file_response/", file_response, name="file_response"),
]
