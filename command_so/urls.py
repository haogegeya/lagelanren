#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 10:23
# @Author  : forhaogege@163.com
from django.urls import path

from .views import ContentView, LabelView, SiteConfigView

app_name = 'command_so'

urlpatterns = [
    path("/content", ContentView.as_view(), name="content"),
    path("/label", LabelView.as_view(), name="label"),
    path("/site", SiteConfigView.as_view(), name="site_confg")
]