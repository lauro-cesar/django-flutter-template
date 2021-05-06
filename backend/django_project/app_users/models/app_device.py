"""[summary]

[description]
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class AppDeviceModel(BaseModel):
    deviceID = models.CharField(
        max_length=512, blank=False, verbose_name="ID do telefone"
    )
    notification_token = models.CharField(
        max_length=512, default="none", blank=False, verbose_name="Token de notificacao"
    )

    usuario = models.ForeignKey(
        "app_users.AppUserModel",
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="devices",
        verbose_name=_("Usuário do telefone"),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Registro de instalação")
        verbose_name_plural = _("Registros de instalações")

    def __str__(self):
        return self.deviceID
