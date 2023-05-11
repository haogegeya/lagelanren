#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 9:49
# @Author  : forhaogege@163.com
from uuid import uuid1

from django.db import models


class ModelBase(models.Model):
    create_time = models.DateTimeField("创建日期", editable=False, auto_now_add=True)
    update_time = models.DateTimeField("更新日期", editable=False, auto_now=True)

    class Meta:
        abstract = True
