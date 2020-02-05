from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer
import json

from .keys import API_KEYS
from .models import Category, Product, Transaction

@csrf_exempt
@parser_classes([JSONParser])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)

        # Return status code 403 if api key isn't valid
        if not (data['api_key'] and data['api_key'] in API_KEYS):
            return HttpResponseForbidden('Invalid API key.')

        # Return status code 400 if fields are missing
        if not (all (field in data for field in ['name', 'category', 'price'])):
            return HttpResponseBadRequest()

        newProduct = Product(name=data['name'], category_id=data['category'], price=data['price'])
        newProduct.save()

        serializer = ProductSerializer(newProduct)
        return JsonResponse(serializer.data, safe=False)

        

@csrf_exempt
def product_category_list(request, category_id):
    if request.method == 'GET':
        products = Product.objects.filter(active=True, category=category_id)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def stats(request):
    products = list(Product.objects.filter(active=True))
    categories = list(Category.objects.values())

    return render(request, 'stats.html', { 'products': products, 'categories': categories })
