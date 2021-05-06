from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class AppLanguageTranslationEntryModel(BaseModel):
    "Modelo para armazenar traduções"

    entry_key = models.ForeignKey(
        "app_settings.AppLanguageEntryKeyModel",
        on_delete=models.CASCADE,
        related_name="translations_entries",
    )

    entry_language = models.ForeignKey(
        "app_settings.AppLanguageModel",
        on_delete=models.CASCADE,
        related_name="translation_values",
    )

    translation_entry_value = models.TextField(
        verbose_name=_("Tradução"),
        help_text=_("String original enviada automaticamente pelo applicativo"),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("String traduzida")
        verbose_name_plural = _("Strings traduzidas")

    def __str__(self):
        return self.translation_entry_value
