from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Brand, Category, Image, Product, ProductModel


class BrandSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Brand model instances
    
    Fields:
        id: An interger field (read only, primary key)
        name: A char field with a maximum length of 255 chars (required, unique validator)
        id: IntegerField(label='ID', read_only=True)
        name: CharField(max_length=255, validators=[<UniqueValidator(queryset=Brand.objects.all())>]
    """
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Category model instances
    
    Fields:
        id: IntegerField(label='ID', read_only=True)
        name: CharField(max_length=255, validators=[<UniqueValidator(queryset=Category.objects.all())>]
    """
    class Meta:
        model = Category
        fields = '__all__'

    
    
class ImageSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Image intances for a specific product.
    
    Fields:
        id: IntegerField(label='ID', read_only=True)
        color: CharField(max_length=255, required=False)
        image: ImageField(max_length=100)
        product: PrimaryKeyRelatedField(queryset=Product.objects.all())
        
    """
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Product instances 
    
    Fields:
        id: IntegerField(label='ID', read_only=True)
        name: CharField(max_length=255)
        description: CharField(style={'base_template': 'textarea.html'})
        brand: PrimaryKeyRelatedField(queryset=Brand.objects.all())
        category: PrimaryKeyRelatedField(queryset=Category.objects.all())
    """
    class Meta:
        model = Product
        fields ='__all__'
        

class ProductModelSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize ProductModel instances for a specific Product inctance
    
    Fields:
        id: IntegerField(label='ID', read_only=True)
        model_name: CharField(max_length=255)
        other_name: CharField(max_length=255)
        release_date: DateField()
        price: DecimalField(decimal_places=2, max_digits=10)
        available_quantity: IntegerField(max_value=9223372036854775807, min_value=-9223372036854775808)
        sold_quantity: IntegerField(max_value=9223372036854775807, min_value=-9223372036854775808, required=False)
        created_at: DateTimeField(read_only=True)
        product: PrimaryKeyRelatedField(queryset=Product.objects.all())
        image: PrimaryKeyRelatedField(allow_null=True, queryset=Image.objects.all(), required=False)
    """
    class Meta:
        model = ProductModel
        fields = '__all__'

