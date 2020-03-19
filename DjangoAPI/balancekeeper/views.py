from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import parser_classes, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, CbkUserSerializer, CategorySerializer, TransactionSerializer
import json

from .models import Category, Product, Transaction, CbkUser


class CategoryView(APIView):

    # Get return all active products, post creates new product

    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class ProductView(APIView):

    # Get return all active products, post creates new product

    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        data = request.data

        try:
            name = data['name']
            category = data['category']
            price = data['price']

        except KeyError:
            return HttpResponse('Bad request.', status=400)

        newProduct = Product(name=name, category_id=category, price=price)
        newProduct.save()

        serializer = ProductSerializer(newProduct)
        return Response(serializer.data)


class CbkUserView(APIView):

    # Get all users / register new user

    permission_classes = [IsAuthenticated]

    def get(self, request):
        cbkusers = CbkUser.objects.all()
        serializer = CbkUserSerializer(cbkusers, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        name = telegram_id = None

        try:
            name = data['name']
            telegram_id = data['telegram_id']

        except KeyError:
            return HttpResponse(400, 'Bad body data')

        # Return status code 400 if user with this telegram already exists
        if CbkUser.objects.filter(telegram_id=telegram_id).exists():
            return HttpResponse('User already exists with that Telegram ID.', status=400)

        # Return status code 400 if telegram_id AND name is missing
        if not bool(name) and not bool(telegram_id):
            return HttpResponse('Bad request.', status=400)

        newCbkUser = CbkUser(name=name, telegram_id=telegram_id)
        newCbkUser.save()

        serializer = CbkUserSerializer(newCbkUser)
        return Response(serializer.data)


class CbkUserDetailView(APIView):

    # Returns user details

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        cbkuser = get_object_or_404(CbkUser, id=id)
        serializerData = CbkUserSerializer(cbkuser).data

        return Response(serializerData)

    def put(self, request, id):
        data = request.data

        cbkuser = get_object_or_404(CbkUser, id=id)

        try:
            cbkuser.name = data['name']
        except KeyError:
            return HttpResponse(400)

        cbkuser.save()

        serializer = CbkUserSerializer(cbkuser)
        return Response(serializer.data)


class TransactionView(APIView):

    # Returns users transaction, adds new ones

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        transactions = Transaction.objects.filter(cbk_user_id=id)
        serializer = TransactionSerializer(transactions, many=True)

        return Response(serializer.data)

    def post(self, request, id):
        data = request.data

        # Check if product and user exist
        if not CbkUser.objects.filter(id=id).exists():
            return HttpResponse('User not found.', status=404)
        
        if not 'product_id' in data or not Product.objects.filter(id=data['product_id']).exists():
            return HttpResponse('Product not found.', status=404)

        newTransaction = Transaction(cbk_user_id=CbkUser.objects.get(id=id), product_id=Product.objects.get(id=data['product_id']))

        newTransaction.save()

        serializer = TransactionSerializer(newTransaction)
        return Response(serializer.data)


def stats(request):

    # Returns some mildly interesting statistics

    products = list(Product.objects.filter(active=True))
    categories = list(Category.objects.values())

    return render(request, 'stats.html', { 'products': products, 'categories': categories })
