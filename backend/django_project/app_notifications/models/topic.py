from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class AppNotificationTopicModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), default="ofertas")

    class Meta(BaseModel.Meta):
        verbose_name = _("Tópico")
        verbose_name_plural = _("Tópicos")

    def __str__(self):
        return self.name
