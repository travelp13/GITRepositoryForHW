from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_orders, name='all_orders'),
    path('done/', views.done_orders, name='done_orders'),
    path('canceled/', views.canceled_orders, name='canceled_orders'),
]
