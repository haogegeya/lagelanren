#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 17:01
# @Author  : forhaogege@163.com

from rest_framework import serializers

from .models import Content


class ContentSeriaslzer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


    def create(self, validated_data):
        # validated_data = validated_data.pop("parent_category")
        labels = validated_data.pop("label")
        content = Content.objects.create(**validated_data)
        for item in labels:
            content.labels.add(item)
        content.save()
        return content

