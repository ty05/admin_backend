from django.urls import path, include

from checkout.views import LinkAPIView, OrderAPIView

urlpatterns = [
    path("link/<str:code>", LinkAPIView.as_view()),
    path("orders", OrderAPIView.as_view()),
]
