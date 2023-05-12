#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 17:01
# @Author  : forhaogege@163.com

from rest_framework import serializers

from .models import Content, Label, SiteConfig


class ContentSeriaslzer(serializers.ModelSerializer):
    labels = serializers.RelatedField(many=True, required=False, queryset=Content.objects.all(), source="label")
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


class LabelSeriaslzer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"


class SiteConfigSeriaslzer(serializers.ModelSerializer):
    total_data = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SiteConfig
        fields = "__all__"

    def get_total_data(self, obj):
        return Content.objects.filter(is_deleted=False).count()


