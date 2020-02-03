from django.contrib import admin

from .models import Category, Product, CbkUser, Transaction

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CbkUser)
admin.site.register(Transaction)
