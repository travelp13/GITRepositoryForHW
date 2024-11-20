from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_authors, name='all_authors'),
    path('top/', views.top_authors, name='top_authors'),
    path('ukraine/', views.ukrainian_authors, name='ukrainian_authors'),
    path('usa/', views.american_authors, name='american_authors'),
    path('top/ukraine/', views.top_ukrainian_authors, name='top_ukrainian_authors'),
]
