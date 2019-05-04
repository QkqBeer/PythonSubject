__author__ = "那位先生Beer"
# from django.contrib import admin
# from django.urls import path
from sessionP import views
from django.conf.urls import url

urlpatterns = [
    url(r'^tijiao/',views.tijiao)
]