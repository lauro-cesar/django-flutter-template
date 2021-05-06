"""[summary]

[description]
"""
from django.contrib import admin
from app_users.models import AppDeviceModel
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin


@admin.register(AppDeviceModel)
class AppDeviceModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["deviceID", "created"]
    ordering = ["-created"]
