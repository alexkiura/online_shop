"""Development settings for myshop project."""

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'online_shop',
        'USER': 'heavy_machinery',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}