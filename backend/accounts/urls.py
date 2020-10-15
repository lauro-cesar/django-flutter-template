from django.urls import path
from . import views


urlpatterns = [path("signin/", views.SignIn.as_view(), name="account-signin")]
