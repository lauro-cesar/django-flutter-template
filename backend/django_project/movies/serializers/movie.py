from rest_framework import serializers
from django.conf import settings
from movies.models import MovieModel


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = ["id", "genres", "title", "description"]
