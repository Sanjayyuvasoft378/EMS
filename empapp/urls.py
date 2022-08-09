
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/',student_info),
    path('add_emp/',add_emp),
]
