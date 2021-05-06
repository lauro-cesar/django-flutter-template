"""[summary]

[description]
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin
from app_settings.models import AppLanguageEntryKeyModel
from django.utils.safestring import mark_safe
from django.contrib.admin import helpers, widgets
from django import forms
from django.db import models
from app_settings.models import AppLanguageTranslationEntryModel




class AdminTextareaWidgetMine(forms.Textarea):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'vLargeTextField', 'rows':'4', **(attrs or {})})



class AppLanguageTranslationEntryModelAdminInline(admin.TabularInline):
    model = AppLanguageTranslationEntryModel
    exclude = ["isPublic", "isActive"]
    extra=2
    formfield_overrides = {
        models.TextField: {'widget': AdminTextareaWidgetMine}
    }



@admin.register(AppLanguageEntryKeyModel)
class AppLanguageEntryKeyModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["entry_key", "entry_original_value", "flag_icon"]
    ordering = ["-created"]
    exclude = ["isPublic", "isActive"]
    formfield_overrides = {
    models.TextField: {'widget': AdminTextareaWidgetMine}
    }
    inlines = [
    AppLanguageTranslationEntryModelAdminInline
    ]



    def flag_icon(self, obj):

        original_language_icon = f"<span><img width=48px src='{obj.entry_original_language.language_icon.url}'></span>"
        traducoes = ' '.join( [ f"<span><img width=48px src='{e.entry_language.language_icon.url}'></span>" for e in obj.translations_entries.all()])


        return mark_safe(  f'{original_language_icon} {traducoes}'  )





    flag_icon.allow_tags = True
    flag_icon.short_description = "Traduções"
