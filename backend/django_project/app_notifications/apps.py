from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppNotificationsConfig(AppConfig):
    name = "app_notifications"
    verbose_name = _("Notificações")

    def ready(self):
        import app_notifications.signals
