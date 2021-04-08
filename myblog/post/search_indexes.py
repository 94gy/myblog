#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gaoyang
# @Date  : 2021/4/6 13:36

from haystack import indexes
from .models import *

#注意格式（模型类名+index）
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #给title，content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')
