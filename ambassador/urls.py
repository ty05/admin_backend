from django.urls import path, include

from ambassador.views import (
    ProductBackendAPIView,
    ProductFrontendAPIView,
    LinkAPIView,
    RankingAPIView,
    StatsAPIView,
)


urlpatterns = [
    path("", include("common.urls")),
    path("product/frontend", ProductFrontendAPIView.as_view()),
    path("product/backend", ProductBackendAPIView.as_view()),
    path("links", LinkAPIView.as_view()),
    path("stats", StatsAPIView.as_view()),
    path("ranking", RankingAPIView.as_view()),
]