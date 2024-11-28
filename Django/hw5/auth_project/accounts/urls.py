from django.urls import path
from .views import *

urlpatterns = [
    path("standard-login/", StandardLoginView.as_view(), name="standard_login"),
    path("custom-login/", CustomLoginView.as_view(), name="custom_login"),
]
