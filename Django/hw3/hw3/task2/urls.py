from django.urls import path
from .views import *

urlpatterns = [
    path("task2/", home_view, name="task2_home"),
    path("task2/luke/", luke_view, name="luke"),
    path("task2/leia/", leia_view, name="leia"),
    path("task2/han/", han_view, name="han"),
]
