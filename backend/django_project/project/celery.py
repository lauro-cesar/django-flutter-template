"""
"""
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
redis_host = os.environ.get("REDIS_HOST", default="localhost")
app = Celery(
    "project",
    broker_url="redis://{redis}:6379".format(redis=redis_host),
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(result_expires=3600, enable_utc=True, timezone="America/Sao_Paulo")

app.autodiscover_tasks()
