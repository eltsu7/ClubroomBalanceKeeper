from rest_framework import serializers
from .models import Product, Category, CbkUser, Transaction
import uuid

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'active']

class CbkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbkUser
        fields = ['id', 'name', 'telegram_id', 'balance']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'active']

class TransactionSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name')
    product_price = serializers.CharField(source='product_id.price')
    cbk_user_name = serializers.CharField(source='cbk_user_id.name')
    class Meta:
        model = Transaction
        fields = ['id', 'product_id', 'product_name', 'product_price', 'cbk_user_id', 'cbk_user_name', 'date', 'description']
