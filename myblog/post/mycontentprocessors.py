#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gaoyang
# @Date  : 2021/4/2 13:25
from django.db.models import Count
from django.db import connection
from .models import *
def getRightInfo(request):
    #获取分类信息
    r_catepost = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')
    #近期文章
    r_recpost = Post.objects.all().order_by('-created')[:3]
    #获取归档信息
    cursor = connection.cursor()
    cursor.execute("select created, count('*') from t_post GROUP BY DATE_FORMAT(created, '%Y-%m');")
    r_filepost = cursor.fetchall()
    return {'r_catepost': r_catepost, 'r_recpost':r_recpost, 'r_filepost':r_filepost}

