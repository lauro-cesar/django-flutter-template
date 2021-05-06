"""[summary]

[description]
"""
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from app_notifications.models import AppNotificationModel
from project.celery import app
import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=AppNotificationModel)
def PostSaveAppNotificationModel( sender, instance, created, using, update_fields, *args, **kwargs):
    if not instance.isProcessed:
        app.send_task("dispatchNotification", [instance.id])

