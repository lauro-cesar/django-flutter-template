from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class AppSettingModel(BaseModel):
    isDefaultSettings = models.BooleanField(
        default=False, verbose_name="Configuração principal"
    )
    terms_of_use_url = models.CharField(
        max_length=512, blank=False, verbose_name="Termos de uso", default="/"
    )
    privacy_police_url = models.CharField(
        max_length=512, blank=False, verbose_name="Politica de privacidade", default="/"
    )
    release_name = models.CharField(verbose_name="Nome do aplicativo", max_length=255)

    languages = models.ManyToManyField("app_settings.AppLanguageModel")


    @property
    def p(self):
        return self.privacy_police_url

    @property
    def t(self):
        return self.terms_of_use_url

    class Meta(BaseModel.Meta):
        verbose_name = _("Configuração do aplicativo")
        verbose_name_plural = _("Configurações do aplicativo")

    def __str__(self):
        return self.release_name
