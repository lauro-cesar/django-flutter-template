from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppUsersConfig(AppConfig):
    name = "app_users"
    verbose_name = _("Relatórios de uso do aplicativo")

    def ready(self):
        import app_users.signals
