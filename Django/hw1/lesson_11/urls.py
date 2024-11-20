from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_1_1),
    path('hello/', views.hello_world),
]
