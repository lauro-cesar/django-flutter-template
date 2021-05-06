from rest_framework import serializers
from django.conf import settings
from app_users.models import AppUserMoreInfoModel
import traceback


class AppUserMoreInfoSerializer(serializers.ModelSerializer):
    cliente_id = serializers.IntegerField(write_only=True)
    imovel_id = serializers.IntegerField()

    class Meta:
        model = AppUserMoreInfoModel
        fields = ["id", "imovel_id", "cliente_id"]
