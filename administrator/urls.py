from django.urls import path, include

from administrator.views import (
    AmbassadorAPIView,
    LinkAPIView,
    OrderAPIView,
    ProductGenericAPIView,
)

urlpatterns = [
    path("", include("common.urls")),
    path("ambassador", AmbassadorAPIView.as_view()),
    path("product", ProductGenericAPIView.as_view()),
    path("product/<str:pk>", ProductGenericAPIView.as_view()),
    path("user/<str:pk>/links", LinkAPIView.as_view()),
    path("orders", OrderAPIView.as_view()),
]
