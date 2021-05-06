"""
[description]
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class StripeSettingsModel(BaseModel):
    """
    [summary]
    [description]
    Extends:
        BaseModel
    """

    name = models.CharField(max_length=144, verbose_name=_("Nome da configuração"))
    publicKey = models.CharField(
        max_length=512, default="", verbose_name=_("Stripe Public Key")
    )
    privateKey = models.CharField(
        max_length=512, default="", verbose_name=_("Stripe Private Key")
    )
    isDefaultSettings = models.BooleanField(default=False, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = _("Conta Stripe")
        verbose_name_plural = _("Contas Stripe")

    def __str__(self):
        return self.name
