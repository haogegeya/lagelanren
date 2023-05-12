from django.db import models

from lagelanren.models import ModelBase
from common.storage import ImageStorage


class Image(ModelBase):
    upload = models.ImageField('图片', blank=True, default=None, null=True, upload_to='%Y%m',
                                  storage=ImageStorage())
    is_deleted = models.BooleanField("是否删除",  default=False)

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'

    def __str__(self):
        return self.img_url
