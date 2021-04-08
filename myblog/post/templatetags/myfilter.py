#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gaoyang
# @Date  : 2021/4/1 20:05
from django.template import Library

register = Library()
@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)