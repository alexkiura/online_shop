"""Production settings."""
import dj_database_url
from .base import *

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')