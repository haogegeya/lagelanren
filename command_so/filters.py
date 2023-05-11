# -*- coding: UTF-8 -*-
"""
@Project ：online_application_backend 
@File    ：filters.py
@Author  ：forhaogege@163.com
@Date    ：2022/12/1 11:55 
"""
import django_filters
from django_filters.rest_framework import FilterSet

from .models import Content


class getContentFilter(FilterSet):
    text = django_filters.CharFilter(field_name="text", lookup_expr="icontains")
    class Meta:
        model = Content
        fields = ()
