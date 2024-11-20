from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('top/', views.top_books, name='top_books'),
    path('free/', views.free_books, name='free_books'),
    path('top/free/', views.top_free_books, name='top_free_books'),
    path('oldschool/', views.oldschool_books, name='oldschool_books'),
]
