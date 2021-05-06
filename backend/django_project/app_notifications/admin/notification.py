"""from django.contrib import admin

[description]
"""
from django.contrib import admin
from app_notifications.models import AppNotificationModel
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin


@admin.register(AppNotificationModel)
class AppNotificationModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["title", "body", "created"]
    ordering = ["-created"]
    exclude = list(BaseModelAdmin.exclude + ["response"])
    filter_horizontal = ["topics"]
