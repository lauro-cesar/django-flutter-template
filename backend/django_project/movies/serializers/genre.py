from rest_framework import serializers
from django.conf import settings
from movies.models import GenreModel



class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ["id", "name"]
