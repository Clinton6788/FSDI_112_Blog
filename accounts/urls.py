from django.urls import path
from posts import views
from .views import LogoutConfirmView

urlpatterns = [
    path("logout/", LogoutConfirmView.as_view(), name="logout_confirm"),
]
