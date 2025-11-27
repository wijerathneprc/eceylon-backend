from django.db import models
# from estore.models import Product 

# Create your models here.
from django.db import models
from generic_feature.models import Ram, Storage, Display, Color, Processor, Battery,Camera

class Laptop(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=255)
    released_year = models.DateField()
    more_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    color = models.ForeignKey(Color, on_delete=models.CASCADE )
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    
    # storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    # display = models.ForeignKey(Display, on_delete=models.CASCADE)
    # processor = models.ForeignKey(Processor,on_delete=models.CASCADE)
    # battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    # camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name 
    