from django.urls import path
from .views import *

urlpatterns = [
    path("", catalog, name="catalog"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
    path("category/<int:pk>/", category_detail, name="category_detail"),
]
