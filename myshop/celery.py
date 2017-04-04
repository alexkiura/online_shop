import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the celery progra,
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshopsettings')

app = Celery('myshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
