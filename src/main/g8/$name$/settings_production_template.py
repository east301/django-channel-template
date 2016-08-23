#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

from $name$.settings_common import *     # NOQA


# ================================================================================
# security
# ================================================================================

SECRET_KEY = ''

DEBUG = False
ALLOWED_HOSTS = ['*']


# ================================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# ================================================================================

STATIC_URL = '/static/'
STATIC_ROOT = ''

MEDIA_URL = '/media/'
MEDIA_ROOT = ''


# ================================================================================
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# ================================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': '',
        'PASSWORD': '',
        'NAME': '$name$_production',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# ================================================================================
# Channels
# ================================================================================

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': '',
        'ROUTING': '$name$.routing.channel_routing'
    }
}


# ================================================================================
# Celery
# ================================================================================

BROKER_URL = ''
CELERY_RESULT_BACKEND = ''
