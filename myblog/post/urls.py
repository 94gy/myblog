#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gaoyang
# @Date  : 2021/3/31 15:37


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.queryAll),
    url(r'^page/(\d+)$', views.queryAll),
    url(r'^post/(\d+)$', views.detail),
    url(r'^category/(\d+)$',views.queryPostByCid),
    url(r'^archive/(\d+)/(\d+)$',views.queryPostByCreated),
]
