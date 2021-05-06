from rest_framework import serializers
from django.conf import settings
from app_users.models import AppUserAnuncioModel
import traceback


class AppUserAnuncioSerializer(serializers.ModelSerializer):
    cliente_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = AppUserAnuncioModel
        fields = ["id", "cliente_id"]
