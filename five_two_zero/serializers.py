#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 17:01
# @Author  : forhaogege@163.com

from rest_framework import serializers

from .models import Content, LeaveMessage


class ContentSeriaslzer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"

class LeaveMessageSeriaslzer(serializers.ModelSerializer):
    class Meta:
        model = LeaveMessage
        fields = "__all__"



