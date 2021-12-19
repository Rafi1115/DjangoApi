from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from inventory.models import Product
from rest_framework import filters

from api import serializers

class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailApiView(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializers = ProductSerializer(product)
        return Response(serializers.data)

from django.db.models import Q
class ProductSearchAPIView(APIView):
    def post(self, resquest, format=None):
        data = self.request.data
        str = data['name']
        q = (Q(name__icontains=str))
        queryset = Product.objects.all()
        queryset = queryset.filter(q)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


         