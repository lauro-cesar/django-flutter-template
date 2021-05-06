"""[summary]

[description]
"""
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from project.authentication import APITokenAuthentication
from project.permissions import IsOwnerOrReadOnly
from django.views.generic import View
from django.http import JsonResponse
from django.middleware import csrf
from django.db import IntegrityError
from django.core.exceptions import ValidationError
import json
import re
from project.pagination import FlutterPagination
from django.contrib.auth import authenticate
from rest_framework.response import Response


from movies.models import MovieModel
from movies.serializers import MovieModelSerializer


class MoviesPagination(FlutterPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response(
            {
                "p": self.page.number,
                "tr": self.page.paginator.count,
                "tp": self.page.paginator.num_pages,
                "d": data,
            }
        )


class MovieModelViewSet(viewsets.ModelViewSet):
    serializer_class = MovieModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = [APITokenAuthentication]
    parser_classes = [JSONParser]
    pagination_class = MoviesPagination

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Activity.objects.none()
