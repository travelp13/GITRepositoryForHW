from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("sales/", sale_list, name="sale_list"),
    path("sales/<slug:slug>/", sale_detail, name="sale_detail"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
    path("delivery/", delivery, name="delivery"),
    path("offer/", offer, name="offer"),
    path("guarantee/", guarantee, name="guarantee"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
]
