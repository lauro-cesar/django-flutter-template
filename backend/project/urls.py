from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views as tokenView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import FlapPagesSitemap
from .views import CustomAuthToken


sitemaps = {"posts": FlapPagesSitemap}

urlpatterns = [
    re_path(r"^admin_tools/", include("admin_tools.urls")),
    path("admin/", admin.site.urls),
    re_path(r"^api-token-auth/", CustomAuthToken.as_view(), name="get-token-auth"),
    path(
        "api/",
        include(
            [
                path("", include("accounts.urls")),
                path("", include("accounts.rest_urls")),
            ]
        ),
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("", include("django.contrib.flatpages.urls")),
]
