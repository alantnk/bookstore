from django.urls import path

from pages.views import HomePageView, AboutPageView, PremiumPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("premium/", PremiumPageView.as_view(), name="premium"),
    path("", HomePageView.as_view(), name="home"),
]
