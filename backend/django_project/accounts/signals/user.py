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
from project.celery import app

from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def PostSaveAccountSignal(
    sender, instance, created, using, update_fields, *args, **kwargs
):
    if True in [created]:
        for signal in User.TASKS.get('on_create',[]):
            app.send_task(signal, [instance.id])
    else:
        for signal in User.TASKS.get('on_save',[]):
            app.send_task(signal, [instance.id])
    