from django.db import models

# Create your models here.
from django.db import models

from lagelanren.models import ModelBase


class Content(ModelBase):
    question_id = models.BigIntegerField('问题ID', blank=True, null=True, default=None)
    city = models.CharField('城市', max_length=16, blank=True, null=True, default=None)
    answer_id = models.BigIntegerField("回答ID", blank=True, null=True, default=None)
    author = models.CharField("用户名", max_length=32, blank=True, null=True, default=None)
    head_url = models.CharField("头像", max_length=128, blank=True, null=True, default=None)
    author_id = models.CharField("用户ID", max_length=64, blank=True, null=True, default=None)
    gender = models.SmallIntegerField("性别", blank=True, null=True, default=None)
    voteup_count = models.IntegerField("赞同次数", default=0, blank=True)
    comment_count = models.IntegerField("回复次数", default=0, blank=True)
    content = models.TextField("内容", blank=True)
    is_picture = models.BooleanField("是否包含图片", default=False, blank=True, null=True)
    is_zhihu = models.BooleanField("是否知乎", default=True)
    is_activate = models.BooleanField("是否激活", default=False)
    is_deleted = models.BooleanField("是否删除",  default=False)

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = '内容'

    def __str__(self):
        return self.answer_id

class Key(ModelBase):
    key = models.CharField('搜索词', max_length=512)
    total = models.IntegerField("次数统计")

    class Meta:
        verbose_name = '搜索词统计'
        verbose_name_plural = '搜索词统计'

    def __str__(self):
        return self.key


    @classmethod
    def update_key_total(cls, value):
        key = cls.objects.filter(key=value).first()
        if key:
            key.total += 1
            key.save()
        else:
            cls.objects.create(key=value, total=1)

class LeaveMessage(ModelBase):
    content = models.TextField("内容")
    is_deleted = models.BooleanField("是否删除",  default=False)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '留言'

    def __str__(self):
        return self.is_deleted