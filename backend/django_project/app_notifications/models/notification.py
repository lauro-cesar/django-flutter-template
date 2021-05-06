from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class AppNotificationModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title "), default="titulo")
    body = models.CharField(
        max_length=255, verbose_name=_("Mensagem "), default="mensagem"
    )
    name = models.CharField(max_length=255, verbose_name=_("Name "), default="nome")
    response = models.TextField(blank=True)
    isProcessed = models.BooleanField(default=False)
    topics = models.ManyToManyField(
        "app_notifications.AppNotificationTopicModel",
        related_name="notifications",
        verbose_name=_("Topicos"),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Notificação")
        verbose_name_plural = _("Notificações")

    def __str__(self):
        return self.title
