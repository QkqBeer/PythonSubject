__author__ = "那位先生Beer"
from django.contrib import admin
from django.urls import path
from databasePractice import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls ),
    url(r'^login/',views.login),
    url(r'^manage-(\w+)/',views.manage),
    url(r'^detail-(?P<id>\d+).html/',views.detail),
]
#超级用户：用户名：qkq； 密码 6988751qkq
