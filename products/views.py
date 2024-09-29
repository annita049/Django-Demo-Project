from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import Product


# Create your views here.
def index(request):
    return HttpResponse("Products Page")

class ProductView (APIView):
    def post (self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

        ## get all/single products
        ## 200ok , 401 unauth (skip), 500 server err,  

    def get(self, request, id=None):
        if id:
            try:
                product = Product.objects.get(id=id)
            except Product.DoesNotExist:
                raise Http404
            serializer = ProductSerializers(product)
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializers(products, many= True)
            return Response(serializer.data)  ## by default returns 200 status

    def put(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the updated product
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404
        serializer = ProductSerializers(product, request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404
        product.delete()
        return Response({"message": "Product Deleted Successfully!"})
        
