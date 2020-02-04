from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Category, Product, Transaction


def category_summary(request):
    categories = list(Category.objects.values())
    
    # Count number of products and add it to category object
    for cat_i in range(len(categories)):
        cat = categories[cat_i]

        try:
            productCount = len(Product.objects.filter(category=cat['id']))
        except ObjectDoesNotExist:
            productCount = 0

        categories[cat_i]['productCount'] = productCount

    return render(request, 'category_list.html', {'categories': categories})


def category_detail(request, id):

    try:
        category = Category.objects.get(id=id)
        products = list(Product.objects.filter(category=category.id).values())
    
    except ObjectDoesNotExist:
        # TODO: over the top 404-page
        return HttpResponse('<h4>Category not found</h4>')

    for prod_i in range(len(products)):
        products[prod_i]['times_bought'] = len(Transaction.objects.filter(product_id=products[prod_i]['id']))

    return render(request, 'category_detail.html', {'category': category, 'products': products})