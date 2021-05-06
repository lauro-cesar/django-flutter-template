from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class AppLanguageEntryKeyModel(BaseModel):

    entry_original_language = models.ForeignKey(
        "app_settings.AppLanguageModel",
        on_delete=models.CASCADE,
        related_name="translation_keys",
    )

    entry_original_value = models.TextField(
        verbose_name="String original",
        help_text=_("String original enviada automaticamente pelo applicativo"),
    )
    entry_description = models.TextField(
        verbose_name=_("Onde encontro isso no app?"),
        help_text=_("Explicação de onde essa string aparece"),
    )
    entry_key = models.CharField(
        verbose_name="ID único",
        max_length=255,
        help_text=_("Deixe em branco para auto criar"),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("String traduzivel")
        verbose_name_plural = _("Strings traduziveis")

    def __str__(self):
        return self.entry_key
