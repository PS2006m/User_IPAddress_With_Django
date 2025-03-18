from django.contrib import admin
from django.urls import path
from .views import my_view
# Create your tests here.
urlpatterns=[
    path('',my_view,name='home')
]