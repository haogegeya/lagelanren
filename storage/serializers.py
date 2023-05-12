#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 17:01
# @Author  : forhaogege@163.com

from rest_framework import serializers

from storage.models import Image

class ImageSeriaslzer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = Image
        fields = "__all__"

    def get_url(self, ojb):
        return ojb.upload.url



