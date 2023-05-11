# -*- coding: UTF-8 -*-
"""
@Project ：steamgo-backend 
@File    ：logging_settings.py
@Author  ：forhaogege@163.com
@Date    ：2022/12/8 13:22 
"""
import logging.handlers
import os

from . import project_root, env


# LOGGING
log_path = project_root('logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'django-info.log'),
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'maxBytes': 1024 * 1024 * 100,
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'django-error.log'),
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'maxBytes': 1024 * 1024 * 100,
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        "django": {
            "handlers": ["info", "error", "console"] if env("LOGGERS_NAME") == "local" else ["info", "error"],
            "level": "INFO" if env("LOGGERS_NAME") == "local" else "DEBUG",
            "propagate": False
        },
        'prod': {
            'handlers': ['info', 'error'],
            'level': 'INFO',
            'propagate': False
        },
        # log 调用时需要当作参数传入
        'local': {
            'handlers': ['info', 'error', "console"],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
LOGGERS_NAME = env("LOGGERS_NAME")