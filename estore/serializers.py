from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Brand, Category, Image, Product, ProductModel


class BrandSerializer(serializers.ModelSerializer):
    """Serialize and deserialize Brand model instances"""
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Serialize and deserialize Category model instances"""
    class Meta:
        model = Category
        fields = '__all__'

    
    
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

    class Meta:
        model = ProductConfig
        fields ='__all__'
        
        
class ProductConfigListSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    image=ImageSerializer(read_only=True)
    
    class Meta:
        model = ProductConfig
        fields ='__all__'
        

    