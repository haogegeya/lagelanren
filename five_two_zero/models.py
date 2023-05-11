from django.db import models

# Create your models here.
from django.db import models

from lagelanren.models import ModelBase


class Content(ModelBase):
    question_id = models.BigIntegerField('问题ID')
    city = models.CharField('城市', max_length=16)
    answer_id = models.BigIntegerField("回答ID")
    author = models.CharField("用户名", max_length=32)
    head_url = models.CharField("头像", max_length=128)
    author_id = models.CharField("用户ID", max_length=64)
    gender = models.SmallIntegerField("性别")
    voteup_count = models.IntegerField("赞同次数", default=0)
    comment_count = models.IntegerField("回复次数", default=0)
    content = models.TextField("内容")
    is_picture = models.BooleanField("是否包含图片", default=False)
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
