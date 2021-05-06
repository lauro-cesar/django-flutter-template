from rest_framework import serializers
from django.conf import settings
from app_users.models import AppUserFavoritoModel
import traceback


class AppUserFavoritoSerializer(serializers.ModelSerializer):
    cliente_id = serializers.IntegerField(write_only=True)
    imovel_id = serializers.IntegerField()

    class Meta:
        model = AppUserFavoritoModel
        fields = ["id", "imovel_id", "cliente_id"]
