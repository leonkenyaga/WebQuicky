from django.shortcuts import render

# Create your views here.
# countries/views.py
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()