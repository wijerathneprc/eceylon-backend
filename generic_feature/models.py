from django.db import models

class Ram(models.Model):
    type = models.CharField(max_length=255)
    capacity=models.DecimalField(max_digits=8, decimal_places=2)

class Storage(models.Model):
    type = models.CharField(max_length=255)
    capacity=models.DecimalField(max_digits=8, decimal_places=2)

class Display(models.Model):
    type = models.CharField(max_length=255)
    resolution = models.CharField()
    screen_size = models.IntegerField()
    description = models.TextField()

class Processor(models.Model):
    name = models.CharField(max_length=255)
    cores = models.IntegerField()
    speed = models.IntegerField()
    graphic = models.CharField(max_length=255)
    description = models.TextField()

class OperatingSystem(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    images = models.CharField(max_length=255)
    description = models.TextField()

class GrapichCard(models.Model):
    name = models.CharField(max_length=255)
    memory = models.DecimalField(max_digits=8, decimal_places=2)
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

class Camera(models.Model):
    PRIMARY, SELFY, WEB = ('p', 'S', 'W')
    CAMERA_TYPE = [(PRIMARY, 'Primary'), (SELFY, 'Selfy'), (WEB, 'Web')]
    type = models.CharField(max_length=1, choices=CAMERA_TYPE, default=WEB)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

class Battery(models.Model):
    type = models.CharField(max_length=255)
    capacity = models.DecimalField(max_digits=8, decimal_places=2)

class SimCard(models.Model):
    name = models.CharField(max_length=255)
