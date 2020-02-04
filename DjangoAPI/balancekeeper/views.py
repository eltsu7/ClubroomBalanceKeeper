from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Product, Transaction

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def product_category_list(request, category_id):
    if request.method == 'GET':
        products = Product.objects.filter(active=True, category=category)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def stats(request):
    # TODO rewrite

    categories = list(Category.objects.values())
    
    # Count number of products and add it to category object
    for cat_i in range(len(categories)):
        cat = categories[cat_i]

        try:
            productCount = len(Product.objects.filter(category=cat['id']))
        except ObjectDoesNotExist:
            productCount = 0

        categories[cat_i]['productCount'] = productCount

    return render(request, 'stats.html', {'categories': categories})
