from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from .views import CustomAuthToken

urlpatterns = [
    re_path(r"^admin_tools/", include("admin_tools.urls")),
    path("admin/", admin.site.urls),
    re_path(r"^api-token-auth/", CustomAuthToken.as_view(), name="get-token-auth"),
    path(
        "accounts/",
        include(
            [
                path("", include("accounts.urls")),
                path("", include("django.contrib.auth.urls")),
            ]
        ),
    ),    
    path(
        "rest-api/",
        include(
            [
                path("v1/accounts/", include("accounts.rest_urls")),
            ]
        ),
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include("django.contrib.flatpages.urls")),
]
