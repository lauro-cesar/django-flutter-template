"""from django.contrib import admin

[description]
"""
from django.contrib import admin
from app_notifications.models import AppNotificationTopicModel
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin


@admin.register(AppNotificationTopicModel)
class AppNotificationTopicModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["name"]
    ordering = ["-created"]
