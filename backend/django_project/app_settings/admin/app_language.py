"""[summary]

[description]
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin
from app_settings.models import AppLanguageModel
from django.utils.safestring import mark_safe
from app_settings.models import AppLanguageEntryKeyModel


from django import forms
from django.db import models

class AdminTextareaWidgetMine(forms.Textarea):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'vLargeTextField', 'rows':'2', **(attrs or {})})



class AppLanguageEntryKeyModelAdminInline(admin.TabularInline):
    model = AppLanguageEntryKeyModel
    exclude = ["isPublic", "isActive"]
    formfield_overrides = {
        models.TextField: {'widget': AdminTextareaWidgetMine}
    }




@admin.register(AppLanguageModel)
class AppLanguageModelAdmin(BaseModelAdmin):
    save_on_top = True
    actions_on_bottom = True
    list_display = ["language_name", "language_code", "flag_icon"]
    ordering = ["-created"]
    exclude = ["isPublic", "isActive"]


    inlines= [
    AppLanguageEntryKeyModelAdminInline
    ]


    def flag_icon(self, obj):
        if obj.language_icon:
            return mark_safe(
                '<img width=48px src="{icon}" />'.format(
                    icon=obj.language_icon.url,
                )
            )
        return "N/A"

    flag_icon.allow_tags = True
    flag_icon.short_description = "Icone"
