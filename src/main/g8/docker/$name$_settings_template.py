#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import os

import pymysql

from $name$.settings.common import *     # NOQA


# ================================================================================
# security
# ================================================================================

SECRET_KEY = '_+tfbe3v%p^i+w)2-pnuyv9w=ij=2jit(&_h%b)g24(1^r_x*0'

DEBUG = False
ALLOWED_HOSTS = ['*']


# ================================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# ================================================================================

STATIC_URL = '/static/'
STATIC_ROOT = '/opt/$name$/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/opt/$name$/media'


# ================================================================================
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# ================================================================================

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'NAME': os.environ['MYSQL_DATABASE'],
        'HOST': 'mysql',
        'PORT': '3306'
    }
}


# ================================================================================
# Channels
# ================================================================================

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'ROUTING': '$name$.routing.channel_routing',
        'CONFIG': {
            'hosts': [
                'redis://redis:6379/0'
            ]
        }
    }
}


# ================================================================================
# Celery
# ================================================================================

BROKER_URL = 'redis://redis:6379/1'
CELERY_RESULT_BACKEND = BROKER_URL
