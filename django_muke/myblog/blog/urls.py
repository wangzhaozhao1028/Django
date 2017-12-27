#coding=utf-8
from django.conf.urls import url
from . import views


# ^$ 严格匹配
urlpatterns = [
    url(r'^$',views.index),
]