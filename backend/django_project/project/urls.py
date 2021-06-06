from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

urlpatterns = [
    re_path(r"^admin_tools/", include("admin_tools.urls")),
    path("admin/", admin.site.urls),
    path("", include("django.contrib.flatpages.urls")),
]
