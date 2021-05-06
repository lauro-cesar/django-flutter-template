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
import qrcode
import hashlib
from django.dispatch import receiver
from django.conf import settings
from .models import Model


@receiver(pre_init, sender=Model)
def PreInit(sender, *args, **kwargs):
    pass


@receiver(post_init, sender=Model)
def PostInit(sender, instance):
    pass


@receiver(pre_save, sender=Model)
def PreSave(sender, instance, raw, using, update_fields):
    pass


@receiver(post_save, sender=Model)
def PostSave(sender, instance, created, using, update_fields):
    pass


@receiver(pre_delete, sender=Model)
def PreDelete(sender, instance, using):
    pass


@receiver(post_delete, sender=Model)
def PostDelete(sender, instance, using):
    pass


@receiver(m2m_changed, sender=Model)
def M2MChanged(sender, instance, action, reverse, model, pk_set, using):
    pass
