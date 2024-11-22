
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('questions/<str:category>/', category_question, name='category_question'),
]
