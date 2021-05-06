from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings

router = DefaultRouter()

router.register(r"settings", views.AppSettingViewSet, basename="settings")


urlpatterns = [path("", include(router.urls))]
