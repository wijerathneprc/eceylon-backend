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

    class Meta:
        model = ProductConfig
        fields ='__all__'
        
        
class ProductConfigListSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    image=ImageSerializer(read_only=True)
    
    class Meta:
        model = ProductConfig
        fields ='__all__'
        
class UserAddressSerializer(serializers.ModelSerializer):
    
    province_display = serializers.CharField(source='get_province_display', read_only=True)
    district_display = serializers.CharField(source='get_district_display', read_only=True)
    
    class Meta:
        model = UserAddress
        fields = ['id','province','district','city','street_line_01', 'street_line_02','postal_code', 'province_display', 'district_display' ]
        


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
        fields = [ 'username','first_name', 'last_name','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user
    