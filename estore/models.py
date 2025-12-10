from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    """ Represents a brand in the online store. """ 
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """ display brand name for string representation"""
        return self.name


class Category(models.Model):
    """ Represents a product category in the online store. """
    name = models.CharField(max_length=255)

    def __str__(self):
        """ display category name for string representation"""
        return self.name


class Product(models.Model):
    """
    Represents a product available for sale in the online store.

    Each product has a name, description, brand, and category.
    These are general details for any product which do not depend on the product category or model.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        """ display product name for string representation"""
        return self.name
  
    
class Image(models.Model):
    """
    Represents an image associated with a specific product.
    
    Each image is linked to a specific product and includes a color description.
    """
    product = models.ForeignKey(Product, related_name='image', on_delete=models.CASCADE)
    color = models.CharField(max_length=255,default='any color' )
    image = models.ImageField(upload_to='images/product')
    
    def __str__(self):
        """ display product name and color name for string representation"""
        return f"{self.product.name} - {self.color}"
    
     
class ProductModel(models.Model):
    """
    Represents a specific model or variant of a product with general details that does not depend on the product category.
    
    Each product model is linked to a general product and may have an associated image.
    each model has its own pricing and stock details.
    """
    product = models.ForeignKey(Product, related_name='product-model', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='product-model-image' on_delete=models.SET_NULL, null=True)
    model_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)  
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.IntegerField()
    sold_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_in_stock(self):
        """
        Checks if the product model is currently in stock.

        Returns:
            bool: True if available_quantity is greater than 0, False otherwise.
        """
        return self.available_quantity > 0
    
    def __str__(self):
        """ display product name and model name for string representation"""
        return f"{self.product.name} - {self.model_name}"