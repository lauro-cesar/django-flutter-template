from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    re_path(r"^admin_tools/", include("admin_tools.urls")),
    path("admin/", admin.site.urls),
    path("curriculos/", include("curriculos.urls")),
    path("", include("django.contrib.flatpages.urls")),
]
