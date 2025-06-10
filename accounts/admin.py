from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdminBase):
    list_display = (
        "email",
        "username",
        "is_superuser",
    )
