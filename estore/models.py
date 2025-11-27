from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Image(models.Model):
    product = models.ForeignKey(Product,related_name='image', on_delete=models.CASCADE)
    color = models.CharField(max_length=255,default='any color' )
    image = models.ImageField(upload_to='images/product', blank=True, null=True)
    

      
class ProductConfig(models.Model):
    product = models.ForeignKey(Product,related_name='config', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    date_created = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    available_quantity = models.IntegerField()



class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    province = models.CharField(max_length=1)
    city = models.CharField(max_length=255)
    street_line_01 = models.CharField(max_length=255)
    street_line_02 = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_config_id = models.ForeignKey(ProductConfig, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    selected = models.BooleanField(default=True)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_config = models.ForeignKey(ProductConfig, on_delete=models.CASCADE)
    delvery_state = models.CharField(max_length=2)
    delivery_estimation = models.DateField()