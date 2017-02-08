import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DBE_online_shop.settings')

app = Celery('DBE_online_shop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
