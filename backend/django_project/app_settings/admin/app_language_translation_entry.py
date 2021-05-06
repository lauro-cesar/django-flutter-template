"""[summary]

[description]
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin
from app_settings.models import AppLanguageTranslationEntryModel
from django.utils.safestring import mark_safe
from django.contrib.admin import helpers, widgets
from django import forms
from django.db import models


class AdminTextareaWidgetMine(forms.Textarea):
    def __init__(self, attrs=None):
        super().__init__(
            attrs={"class": "vLargeTextField", "rows": "4", **(attrs or {})}
        )


@admin.register(AppLanguageTranslationEntryModel)
class AppLanguageTranslationEntryModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["entry_key", "translation_entry_value", "flag_icon"]
    ordering = ["-created"]
    exclude = ["isPublic", "isActive"]

    formfield_overrides = {models.TextField: {"widget": AdminTextareaWidgetMine}}

    def flag_icon(self, obj):
        if obj.entry_language.language_icon:
            return mark_safe(
                '<img width=48px src="{icon}" />'.format(
                    icon=obj.entry_language.language_icon.url,
                )
            )
        return "N/A"

    flag_icon.allow_tags = True
    flag_icon.short_description = "Icone"
