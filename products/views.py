from django.shortcuts import render
from django.core import serializers
from rest_framework. decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer



@api_view(['GET'])
def list_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def create_view(request):
#     pass