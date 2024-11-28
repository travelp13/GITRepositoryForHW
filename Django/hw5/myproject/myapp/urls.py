from django.urls import path
from .views import *

urlpatterns = [
    path("", main_page, name="main_page"),
    path("create/", create_product, name="create_product"),
    path("list/", product_list, name="product_list"),
    path("submit-review/", submit_review, name="submit_review"),
    path("review-success/", review_success, name="review_success"),
]
