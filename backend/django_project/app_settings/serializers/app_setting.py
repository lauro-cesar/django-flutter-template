"""[summary]

[description]

Variables:
    ) {[type]} -- [description]
"""

from rest_framework import serializers
from django.conf import settings
from app_settings.models import AppSettingModel
import traceback


class AppSettingModelSerializer(serializers.ModelSerializer):
    """
    [Maps]
    p=privacy url
    t=Terms url
    """

    class Meta:
        model = AppSettingModel
        fields = ["p", "t"]
