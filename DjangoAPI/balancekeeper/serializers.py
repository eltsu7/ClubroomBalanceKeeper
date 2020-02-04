from rest_framework import serializers
from .models import Product, Category
import uuid

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price']