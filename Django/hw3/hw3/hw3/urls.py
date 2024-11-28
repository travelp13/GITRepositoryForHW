from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("task1.urls")),
    path("", include("task2.urls")),
    path("", include("task3.urls")),
    path("", include("task4.urls")),
]
