"""[summary]

[description]
"""
"""

[description]
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin
from django.utils.safestring import mark_safe
from stripesettings.models import StripeSettingsModel


@admin.register(StripeSettingsModel)
class StripeSettingsModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["name", "isDefaultSettings"]
    ordering = ["-created"]
    exclude = [""]
