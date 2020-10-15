from rest_framework import serializers
from django.contrib.auth import get_user_model


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = [
            "password",
            "username",
            "email",
            "first_name",
            "last_name",
            "id",
            "authToken",
        ]
        write_only_fields = ["password"]
        read_only_fields = [
            "is_staff",
            "is_superuser",
            "is_active",
            "authToken",
            "id",
            "testUser",
        ]

    def create(self, validated_data):
        user = super(AccountSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
