"""
"""
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    save_on_top = True
    list_filter = ["is_superuser"]
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
