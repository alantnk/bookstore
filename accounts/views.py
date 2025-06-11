from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import AccountCreationForm


class SignupPageView(generic.CreateView):
    form_class = AccountCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
