from django.views.generic import TemplateView
from allauth.account.decorators import verified_email_required
from django.utils.decorators import method_decorator


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class PremiumPageView(TemplateView):
    template_name = "premium.html"

    @method_decorator(verified_email_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
