from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    AdminUserCreationForm,
)


class AccountCreationForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "is_staff",
        )


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
