# -*- coding: UTF-8 -*-
"""
@Project ：dockercomposeManager 
@File    ：base_settings.py
@Author  ：forhaogege@163.com
@Date    ：2023/3/15 20:13 
"""
from . import env, project_root

# export
IMPORT_EXPORT_USE_TRANSACTIONS = True

DEBUG = env.bool('DEBUG', True)  # False if not in os.environ

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'HOST': env('DB_HOST'),
        'PORT': env.int('DB_PORT'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'POOL_OPTIONS': {
            'POOL_SIZE': 60,
            'MAX_OVERFLOW': 80,
            'RECYCLE': 60 * 5
        },
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# Celery Config
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_TIMEZONE = "Asia/Shanghai"
CELERY_ENABLE_UTC = False
DJANGO_CELERY_BEAT_TZ_AWARE = False

ASGI_APPLICATION = 'dockercomposeManager.asgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
# APPEND_SLASH = False

# 上传文件位置
MEDIA_ROOT = env("UPLOAD_PATH")
MEDIA_URL = '/two/media/'
