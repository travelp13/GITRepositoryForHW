from django.urls import path
from .views import *
urlpatterns = [
    path("", main),
    path("send_order/", send_order),
]