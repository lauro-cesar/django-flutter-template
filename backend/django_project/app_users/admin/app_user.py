"""[summary]

[description]
"""
from django.contrib import admin
from app_users.models import AppUserModel
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin


@admin.register(AppUserModel)
class AppUserModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["nome", "email", "telefone", "created"]
    ordering = ["-created"]
    exclude = ["cliente_id"]
