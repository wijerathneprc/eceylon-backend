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
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField()
    sold_count = models.IntegerField(default=0)
    warranty_period = models.IntegerField()  # in months
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

class UserAddress(models.Model):
    PROVINCE_CHOICES = [
        ('CP', 'Central Province'),('EP', 'Eastern Province'),('NCP', 'North Central Province'), ('NP', 'Northern Province'),('NWP', 'North Western Province'),('SMP', 'Sabaragamuwa Province'),('SP', ' Southern Province'),('UP', ' Uva Province'),('WP', 'Western Province')
    ]
    DISTRICT_CHOICES =[
        ('1','Jaffna'),('2','Kilinochchi'),('3','Mannar'),('4','Mullaitivu'),('5','Vavuniya'),('6','Puttalam'),('7','Kurunegala'),('8','Gampaha'),('9','Colombo'),('10','Kalutara'),('11','Trincomalee'),('12','Batticaloa'), ('13','Ampara'),('14','Badulla'), ('15','Monaragala'),('16','Hambantota'),('17','Matara'),('18','Galle'),('19','Anuradhapura'),('20','Polonnaruwa'),('21','Matale'),('22','Kandy'),('23','Nuwara Eliya'),('24','Kegalle'),('25','Ratnapura')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    province = models.CharField(max_length=3, choices=PROVINCE_CHOICES, default='CP')
    district = models.CharField(max_length=2, choices=DISTRICT_CHOICES, default='1')
    city = models.CharField(max_length=255)
    street_line_01 = models.CharField(max_length=255)
    street_line_02 = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    default=models.BooleanField(default=False)
    
    
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