
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets, generics

from .models import Brand, Category, Product, Image, ProductModel
from .serializers import BrandSerializer, CategorySerializer,ProductSerializer,ImageSerializer, ProductModelSerializer



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.all()
        print(self.request.data)
        return queryset
  
    
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
 
    
class ProductModelViewSet(viewsets.ModelViewSet):
    
    serializer_class =  ProductModelSerializer
    
    def get_queryset(self):
        queryset = ProductModel.objects.all()
        return queryset
    
    def perform_create(self, serializer):
    
        serializer.save(idd = self.request.data['product']['id'] )
        print(self.request.data)
    
 