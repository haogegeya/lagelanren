from django.db import models

from lagelanren.models import ModelBase
from .storage import ImageStorage


class Label(ModelBase):
    name = models.CharField('标签名', max_length=50)
    is_deleted = models.BooleanField("是否删除",  default=False)


    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Content(ModelBase):
    labels = models.ManyToManyField(Label, related_name="contents")
    summary = models.CharField("摘要", max_length=128)
    text = models.TextField("内容")
    is_activate = models.BooleanField("是否展示", default=False)
    is_deleted = models.BooleanField("是否删除",  default=False)
    class Meta:
        verbose_name = '内容'
        verbose_name_plural = '内容'

    def __str__(self):
        return self.summary

class Image(ModelBase):
    upload = models.ImageField('图片', blank=True, default=None, null=True, upload_to='%Y%m',
                                  storage=ImageStorage())
    is_deleted = models.BooleanField("是否删除",  default=False)

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'

    def __str__(self):
        return self.img_url

class SiteConfig(ModelBase):
    background = models.ImageField('图片', blank=True, default=None, null=True, upload_to='%Y%m',
                                  storage=ImageStorage())
    total_query = models.IntegerField("查询总数")
    total_query_success = models.IntegerField("有效查询总数")
    class Meta:
        verbose_name = '站点'
        verbose_name_plural = '站点'

    def __str__(self):
        return str(self.total_query) + "/" + str(self.total_query_success)

    @classmethod
    def update_query(cls, is_null=True):
        print(is_null)
        for item in cls.objects.all():
            item.total_query += 1
            if not is_null:
                item.total_query_success += 1
            item.save()
