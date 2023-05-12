# -*- coding: UTF-8 -*-
"""
@Project ：online_application_backend 
@File    ：filters.py
@Author  ：forhaogege@163.com
@Date    ：2022/12/1 11:55 
"""
import django_filters
from django.db.models import Q
from django_filters.rest_framework import FilterSet

from .models import Content, Key


class getContentFilter(FilterSet):
    # content = django_filters.CharFilter(field_name="content", lookup_expr="icontains")
    q = django_filters.CharFilter(method='my_custom_filter', label="关键词")
    class Meta:
        model = Content
        fields = ("q", )

    def my_custom_filter(self, queryset, name, value):
        for key in value.split(' '):
            key = key.strip()
            queryset = queryset.filter(content__icontains=key)
        return queryset