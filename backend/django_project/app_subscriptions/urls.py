from django.urls import path,include, re_path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.Index.as_view())
]
