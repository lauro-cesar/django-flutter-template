from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppSubscriptionsConfig(AppConfig):
    name = "app_subscriptions"
    verbose_name = _("Assinaturas")

    def ready(self):
        import app_subscriptions.signals
