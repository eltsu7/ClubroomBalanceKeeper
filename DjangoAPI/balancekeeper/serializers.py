from rest_framework import serializers
from .models import Product, Category, CbkUser
import uuid

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price']

class CbkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbkUser
        fields = ['id', 'name', 'telegram_id']