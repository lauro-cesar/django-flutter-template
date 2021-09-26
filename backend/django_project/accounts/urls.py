from django.urls import path, re_path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path("create/", views.AccountCreate.as_view(), name="account-create"),    
    path(
        "profile/",
        login_required(views.AccountProfile.as_view()),
        name="account-profile",
    ),   
    path(
        "signin/validate/<uidb64>/<token>/",
        views.AccountSigninValidate.as_view(),
        name="account-signin-validate",
    ),
]
