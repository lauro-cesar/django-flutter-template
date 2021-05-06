"""[summary]

[description]

Variables:
    ) {[type]} -- [description]
    ) {[type]} -- [description]
"""

import base64
from django.db.models import OuterRef, Subquery
import traceback
from django.conf import settings


from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.response import Response
from project.pagination import FlutterPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from project.permissions import IsOwnerOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.parsers import JSONParser
from rest_framework_xml.parsers import XMLParser
from app_settings.serializers import AppSettingModelSerializer
from app_settings.models import AppSettingModel


class SettingsPagination(FlutterPagination):
    page_size = 1500
    page_size_query_param = "page_size"
    max_page_size = 1500

    def get_paginated_response(self, data):
        return Response(
            {
                "p": self.page.number,
                "tr": self.page.paginator.count,
                "tp": self.page.paginator.num_pages,
                "d": data,
            }
        )


class AppSettingViewSet(viewsets.ModelViewSet):
    serializer_class = AppSettingModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]
    parser_classes = [XMLParser, JSONParser]
    renderer_classes = [XMLRenderer, JSONRenderer]
    pagination_class = SettingsPagination

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            "request": self.request,  # request object is passed here
            "format": self.format_kwarg,
            "view": self,
        }

    def get_queryset(self):
        results = AppSettingModel.objects.filter(
            isActive=True, isPrimary=True
        ).order_by("-created")

        return results
