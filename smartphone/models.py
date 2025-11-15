from django.db import models

# Create your models here.
class Ram(models.Model):
    type = models.CharField(max_length=255)
    capacity=models.IntegerField()

class Storage(models.Modle):
    type = models.CharField(max_length=255)
    capacity=models.IntegerField()

class Display(models.Model):
    type = models.CharField(max_length=255)
    resolution = models.CharField()
    screen_size = models.CharField()
    description = models.TextField()

class Processor(models.Model):
    type = models.CharField(max_length=255)
    speed = models.CharField()
    description = models.TextField()

class OperatingSystem(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    images = models.CharField(max_length=255)
    description = models.TextField()

class Grapich(models.Model):
    type = models.CharField(max_length=255)
    speed = models.CharField()
    description = models.TextField()

class Connectivity(models.Model):
    type = models.CharField(max_length=255)
    speed = models.CharField()
    description = models.TextField()

class Color(models.Model):
    name = models.CharField(max_length=255)
    hash_code = models.CharField(max_length=255)
    images = models.CharField(max_length=255)

class Warranty(models.Model):
    name = models.CharField(max_length=255)
    hash_code = models.CharField(max_length=255)
    valid_period = models.DateTimeField()
    images = models.CharField(max_length=255)
    
class Shipping(models.Model):
    name = models.CharField(max_length=255)
    hash_code = models.CharField(max_length=255)
    valid_period = models.DateTimeField()

class Camera(models.Model):
    name = models.CharField(max_length=255)
    hash_code = models.CharField(max_length=255)
    valid_period = models.DateTimeField()

class Battery(models.Modles):
    name = models.CharField(max_length=255)
    hash_code = models.CharField(max_length=255)
    valid_period = models.DateTimeField()

class SimCard(models.Model):
    name = models.CharField(max_length=255)
    hash_code = models.CharField(max_length=255)
    valid_period = models.DateTimeField()


class Smartphone(models.Model):
    model = models.CharField(max_length=255)
    most_suitable_for = models.TextField()
    more_description = models.TextField()
    released_year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    sotorage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    display = models.ForeignKey(Display, on_delete=models.CASCADE)