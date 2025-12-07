
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets, generics

from .serializers import BrandSerializer, CategorySerializer, ImageSerializer, UserRegisterSerializer, UserAddressSerializer, CartSerializer, OrderSerializer
from .models import Brand, Category, Image, ProductConfig, UserAddress, Cart, Order

from . import serializers
    
class CategoryCreateView(generics.CreateAPIView):
    queryset =Category.objects.all()
    serializer_class= CategorySerializer
    
class CategoryUpdateView(generics.UpdateAPIView):
    queryset =Category.objects.all()
    serializer_class= BrandSerializer
    
class CategoryDeleteView(generics.DestroyAPIView):
    queryset =Category.objects.all()
    serializer_class= CategorySerializer
    
class CategoryListView(generics.ListAPIView):
    serializer_class= CategorySerializer
    
    def get_queryset(self):
        queryset = Category.objects.all()
        cat = self.request.query_params.get('param')
        if cat:
            queryset = queryset.filter(name__startswith=cat)
        return queryset


class BrandCreateView(generics.CreateAPIView):
    queryset =Brand.objects.all()
    serializer_class= BrandSerializer
    
class BrandDeleteView(generics.DestroyAPIView):
    queryset =Brand.objects.all()
    serializer_class= BrandSerializer
    
class BrandUpdateView(generics.UpdateAPIView):
    queryset =Brand.objects.all()
    serializer_class= BrandSerializer
    
class BrandListView(generics.ListAPIView):
    serializer_class= BrandSerializer
    
    def get_queryset(self):
        queryset = Brand.objects.all()
        param = self.request.query_params.get('param')
        if param:
            queryset = queryset.filter(name__startswith=param)
        return queryset


class ImageCreateView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
class ImageUpdateView(generics.UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
class ImageDeleteView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageListView(generics.ListAPIView):
    serializer_class = ImageSerializer
    def get_queryset(self):
        queryset = Image.objects.all()
        param = self.request.query_params.get('param')
        queryset = queryset.filter(product_id=param)
        return queryset       


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserUdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
    
class UserAddressCreateView(generics.CreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer 
    
    def perform_create(self, serializer):
        print(self.request.user.id)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else: print(serializer.errors)
    
class UserAddressListView(generics.ListAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer 
    
class UserAddressUpdateView(generics.UpdateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer 
    
    def perform_create(self, serializer):
        print(self.request.user.id)
        if serializer.is_valid():
            print(self.request.user.id)
            serializer.save(user=self.request.user)
        else: print(serializer.errors)
    
class UserAddressDeleteView(generics.DestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer 
      
class UserAddressRetrieveView(generics.RetrieveAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer 
    
    
class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartRetrieveView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartUpdateView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CarDeleteView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
  
    
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
      
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    