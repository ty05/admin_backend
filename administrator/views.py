from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from administrator.serializers import LinkSerializer, OrderSerializer, ProductSerializer
from common.serializers import UserSerializer
from rest_framework.response import Response
from cors.models import Link, Order, Product, User
from rest_framework import generics, mixins, serializers
from rest_framework.permissions import IsAuthenticated
from cors.authentication import JWTAuthentication
from django.core.cache import cache

# Create your views here.
class AmbassadorAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _):
        ambassadors = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassadors, many=True)
        return Response(serializer.data)


class ProductGenericAPIView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)

        return self.list(request)

    def post(self, request):
        response = self.create(request)
        cache.delete("products_frontend")
        cache.delete("product_backend")
        return response

    def put(self, request, pk=None):
        response = self.partial_update(request, pk)
        cache.delete("products_frontend")
        cache.delete("product_backend")
        return response

    def delete(self, request, pk=None):
        response = self.destory(request, pk)
        cache.delete("products_frontend")
        cache.delete("product_backend")
        return response


class LinkAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        links = Link.objects.filter(user_id=pk)
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)


class OrderAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(complete=True)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
