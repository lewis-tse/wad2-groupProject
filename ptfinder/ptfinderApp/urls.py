from django.urls import path
from ptfinderApp import views

app_name = 'ptfinder'

urlpatterns = [
    path('', views.index, name="index"),
]