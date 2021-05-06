""" [summary]

[description]
"""
from django.contrib import admin
from app_subscriptions.models import AppSubscriptionPlanModel
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin


@admin.register(AppSubscriptionPlanModel)
class AppSubscriptionPlanModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["label", "created"]
    ordering = ["-created"]
