__author__ = "那位先生Beer"
from django.contrib import admin
from django.urls import path
from cmdb import views
from django.conf.urls import url

urlpatterns = [
    # path('admin/', admin.site.urls), #path（访问地址，方法）
    path('Login', views.Login),
    path('home', views.home),
    path('register',views.register),
    path('cbv',views.Cbv.as_view()),
    path('index/',views.index),
    url(r'^detail-(\d+).html',views.detail),
    url(r'^page',views.page),
    url(r'^registerAjax',views.registerAjax),
    url(r'^iframe',views.iframe),
    url(r'^check_code',views.checkCode)
]
