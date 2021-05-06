from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from celery import shared_task
from project.celery import app

import logging


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def postSaveUser(sender, instance=None, created=False, **kwargs):
    if created:
        app.send_task("createToken", [instance.id])
    app.send_task("createOrUpdateAppUser", [instance.id])
