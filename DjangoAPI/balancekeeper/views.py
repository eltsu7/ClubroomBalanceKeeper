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


def category_detail(request, id):

    try:
        category = Category.objects.get(id=id)
        products = Product.objects.filter(category=category.id)
        return render(request, 'category_detail.html', {'category': category, 'products': products})
    
    except ObjectDoesNotExist:
        # TODO: over the top 404-page
        return HttpResponse('<h4>Category not found</h4>')
