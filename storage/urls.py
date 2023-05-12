#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 10:23
# @Author  : forhaogege@163.com
from django.urls import path

from .views import ImageView

app_name = 'command_so'

urlpatterns = [
    path("/image", ImageView.as_view(), name="image"),
]