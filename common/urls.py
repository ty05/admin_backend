from django.urls import path, include
from .views import (
    LoginAPIView,
    LogoutAPIView,
    ProfileAPIView,
    ProfilePasswordAPIView,
    RegsiterAPIView,
    UserAPIView,
)

urlpatterns = [
    path("register", RegsiterAPIView.as_view()),
    path("login", LoginAPIView.as_view()),
    path("user", UserAPIView.as_view()),
    path("logout", LogoutAPIView.as_view()),
    path("users/info", ProfileAPIView.as_view()),
    path("users/password", ProfilePasswordAPIView.as_view()),
]
