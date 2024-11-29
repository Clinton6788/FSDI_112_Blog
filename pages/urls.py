from django.urls import path
from .views import HomePageView, AboutPageView, AccountLogoutView


urlpatterns = [
    path("", HomePageView.as_view(),name="home"),
    path("about/", AboutPageView.as_view(),name="about"),
    path("logout/", AccountLogoutView.as_view(), name="logout"),
]