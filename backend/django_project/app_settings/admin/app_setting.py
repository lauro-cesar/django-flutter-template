"""[summary]

[description]
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin
from app_settings.models import AppSettingModel


@admin.register(AppSettingModel)
class AppSettingModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["release_name", "created"]
    ordering = ["-created"]
    filter_horizontal = ["languages"]
