from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppSettingsConfig(AppConfig):
    name = "app_settings"
    verbose_name = _("Configurações do aplicativo")

    def ready(self):
        import app_settings.signals
