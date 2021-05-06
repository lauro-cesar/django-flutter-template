"""[summary]

[description]
"""
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_init,
    post_init,
    pre_delete,
    post_delete,
    m2m_changed,
)
import hashlib
from django.dispatch import receiver
from django.conf import settings
from app_users.models import AppUserAnuncioModel
from celery import shared_task
from project.celery import app


@receiver(post_save, sender=AppUserAnuncioModel)
def PostSave(sender, instance, created, using, update_fields, **kwargs):
    if not instance.sent:
        app.send_task("sentAnuncio", [instance.id])
