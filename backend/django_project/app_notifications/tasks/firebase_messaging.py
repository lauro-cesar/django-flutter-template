"""[summary]

[description]
"""
from app_notifications.models import AppNotificationModel
from firebase_admin import messaging
import firebase_admin
from celery import shared_task
from django.utils.encoding import smart_str, smart_text
import traceback
import time
import hashlib
import uuid
from io import BytesIO
import json
import logging
logger = logging.getLogger(__name__)


@shared_task(name="dispatchNotification", max_retries=2, soft_time_limit=45)
def dispatchNotification(notificationID):
    notification = AppNotificationModel.get_or_none(pk=notificationID)

    if notification:
        responses = []
        for topic in notification.topics.all():
            message = messaging.Message(
                topic=topic.name,
                notification=messaging.Notification(
                    title="{title}".format(title=notification.title),
                    body="{body}".format(body=notification.body),
                ),
            )
            responses.append(messaging.send(message))
        notification.response = "/n/t/r".join(responses)
        notification.processed = True
        notification.save()

