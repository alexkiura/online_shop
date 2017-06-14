"""Development settings for myshop project."""

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'online_shop',
        'USER': 'kiura',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}