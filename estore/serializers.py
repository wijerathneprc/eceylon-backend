from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product, Brand, Category, Image, ProductConfig, UserAddress, Cart, Order


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
    def validate_name(self, value):
        if Brand.objects.filter(name=value).exists():
            raise serializers.ValidationError("Can't have same value")
        return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Can't have same value")
        return value
    
    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        queryset=Brand.objects.all(),
        slug_field='name',
    )
    
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = Product
        fields ='__all__'

class ProductConfigSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    image=ImageSerializer()
    
    class Meta:
        model = ProductConfig
        fields ='__all__'
        
class UserAddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAddress
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    product_config_id = ProductConfigSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
 
 