from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    AdminUserCreationForm,
)


class CustomUserCreationForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "is_staff",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
