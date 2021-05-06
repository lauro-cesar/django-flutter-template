from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StripesettingsConfig(AppConfig):
    name = "stripesettings"
    verbose_name = _("Stripesettings")

    def ready(self):
        import stripesettings.signals
