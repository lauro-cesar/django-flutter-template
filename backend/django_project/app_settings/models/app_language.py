from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel

# LANGUAGE_CODE = "pt-br"
# LANGUAGES = [("pt-br", "Português")]




class AppLanguageModel(BaseModel):
    language_name = models.CharField(verbose_name="Nome da linguagem", max_length=255)
    language_code = models.CharField(verbose_name="Código da linguagem", max_length=8)
    language_icon = models.ImageField(upload_to="icons/languages/", blank=True, null=True)


    class Meta(BaseModel.Meta):
        verbose_name = _("Idioma")
        verbose_name_plural = _("Idiomas")

    def __str__(self):
        return self.language_name
