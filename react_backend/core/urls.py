from .views import DoctorUpdate, login
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('login', login,name='login'),
    path('update', DoctorUpdate,name='update'),
]