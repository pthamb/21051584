from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('<str:number_id>/', views.calculate_average, name='calculate_average'),
]