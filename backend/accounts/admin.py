from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    save_on_top = True
    list_filter = ["testUser", "is_superuser"]
    list_display = ["username", "testUser", "first_name", "last_name", "email"]
