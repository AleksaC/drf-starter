import os
import sys

from celery import Celery

# This will prevent celery from crashing if there are imports across django apps
# Those imports of the form from project.some_app import ...
sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.prod")

app = Celery("server")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
