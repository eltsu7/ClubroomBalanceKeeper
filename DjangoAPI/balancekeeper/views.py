from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Category, Product

def category_summary(request):
    categories = list(Category.objects.values())
    
    # Count number of products and add it to category object
    for catIndex in range(len(categories)):
        cat = categories[catIndex]

        try:
            productCount = len(Product.objects.filter(category=cat['id']))
        except ObjectDoesNotExist:
            productCount = 0

        categories[catIndex]['productCount'] = productCount

    return render(request, 'category_list.html', {'categories': categories})
    