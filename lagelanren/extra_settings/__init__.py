#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 9:45
# @Author  : forhaogege@163.com
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
current = environ.Path(__file__)
project_root = current - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env()
APP_ENV = env.str('STEAMGO_ENV', 'local')
env_file = project_root("%s.env" % APP_ENV)
env.read_env(env_file)