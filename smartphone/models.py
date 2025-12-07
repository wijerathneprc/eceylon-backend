from django.db import models
from estore.models import ProductConfig, Product 


    
class Smartphone(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='smartphone')
    os = models.CharField(max_length=100)
    screen_type = models.CharField(max_length=100)  
    resolution = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    battery_capacity = models.IntegerField()  # in mAh  
    camera_specs = models.CharField(max_length=255)
    def __str__(self):
        return 'Smartphone'
    
    
class SmartphoneConfig(models.Model):
    product_config = models.OneToOneField(ProductConfig, on_delete=models.CASCADE, related_name='smartphone_config')
    smartphone = models.ForeignKey(Smartphone, on_delete=models.CASCADE, related_name='configs')    
    color = models.CharField(max_length=50)
    storage_capacity = models.IntegerField()  # in GB   
    ram = models.IntegerField()  # in GB
    
    def __str__(self):
        return f"{self.smartphone} - {self.color} - {self.storage_capacity}GB"
    