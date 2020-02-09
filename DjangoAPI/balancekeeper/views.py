from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CbkUserSerializer
import json

from .keys import API_KEYS
from .models import Category, Product, Transaction, CbkUser


class CbkBaseClass(APIView):

    # Base class for models views in CBK

    def isValidKey(self, request):
        if 'api_key' in request.data:
            return request.data['api_key'] in API_KEYS
        else:
            return False


class ProductView(CbkBaseClass):

    # Get return all active products, post creates new product

    def get(self, request):
        products = Product.objects.filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    @parser_classes([JSONParser])
    def post(self, request):

        # Return status code 403 if api key isn't valid
        if not self.isValidKey(request):
            return HttpResponse('Invalid API key.', status=403)

        data = request.data

        # Return status code 400 if fields are missing
        if not (all (field in data for field in ['name', 'category', 'price'])):
            return HttpResponse('Bad request.', status=400)

        newProduct = Product(name=data['name'], category_id=data['category'], price=data['price'])
        newProduct.save()

        serializer = ProductSerializer(newProduct)
        return Response(serializer.data)

class CbkUserView(CbkBaseClass):

    # Get all users / register new user

    def get(self, request):

        # Return status code 403 if api key isn't valid
        if not self.isValidKey(request):
            return HttpResponse('Invalid API key.', status=403)

        cbkusers = CbkUser.objects.all()
        serializer = CbkUserSerializer(cbkusers, many=True)
        return Response(serializer.data)


def stats(request):
    products = list(Product.objects.filter(active=True))
    categories = list(Category.objects.values())

    return render(request, 'stats.html', { 'products': products, 'categories': categories })
