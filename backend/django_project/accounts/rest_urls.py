from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views


router = DefaultRouter()

router.register(r"profile", views.ProfileViewSet, basename="profile")
urlpatterns = [path("", include(router.urls))]
