#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 10:23
# @Author  : forhaogege@163.com
from django.urls import path

from .views import ContentView, index, site_total, LeaveMessageView

app_name = 'five_two_zero'

urlpatterns = [
    path("/data", ContentView.as_view(), name="content"),
    path("/message", LeaveMessageView.as_view(), name="leave_message"),
    path("/site", site_total, name="site_total"),
    path("/index", index, name="index"),
]