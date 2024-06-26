# webquicky/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ "id", "productname","productdescription1", "productdescription2", "productnumber" ]