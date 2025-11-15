from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product, Brand, Category

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
    


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ["name", "description", "base_price", "date_created", "brand", "category"]

    def create(self, validated_data):
        
        print(validated_data)
        brand =Brand.objects.create(name=validated_data['brand']['name'])
        
    
        cat = Category.objects.create(name = validated_data['category']['name'])
        prod = Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            base_price = validated_data['base_price'],
            brand = brand,
            category = cat
        )

        return prod


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
        