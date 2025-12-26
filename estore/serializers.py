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
        
        
class ProductModeldSerializer(serializers.ModelSerializer):
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
        # depth = 2

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
    product = ProductSerializer()
    
    class Meta:
        model = ProductModel
        fields = '__all__'

    def create(self, validated_data):
        """
        Create new ProductModel instances
        
        Args:
            validated_data (dict): a dictionary of key value pair represting a instance of ProductModel
            
        Return:
            ProductModel
        """
        print(validated_data)
        product_data = validated_data.pop('product')
    
        if 'idd' in validated_data:
            idd = validated_data.pop('idd')
            product = Product.objects.get(pk=idd)
            
        else:
            product = Product.objects.create(**product_data)
        
        product_model = ProductModel.objects.create(product = product, **validated_data)
        return product_model
    
    def update(self, instance, validated_data):
        """
        Update a instance of ProductModel
        
        Args:
            instance (ProductModel): instance of ProductModel
            validated_data (dict): a dictionary of validated data
        Returns:
            ProductModel
        """
        product_data = validated_data.pop('product')
        print(product_data)
        product = instance.product
        product.name = product_data.get('name', product.name)
        product.description = product_data.get('description',product.description)
        product.brand = product_data.get('brand', product.brand)
        product.category = product_data.get('category', product.category)
        product.save()
    
        instance.model_name = validated_data.get('model_name')
        instance.other_name = validated_data.get('other_name')
        instance.released_date = validated_data.get('released_date')
        instance.price = validated_data.get('price')
        instance.available_quantity = validated_data.get('available_quantity')
        instance.sold_quantity = validated_data.get('sold_quantity')
        instance.image = validated_data.get('image')
        instance.save()
       
        return instance

        