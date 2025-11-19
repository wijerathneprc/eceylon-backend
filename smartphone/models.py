from django.db import models
from generic_feature import Ram, Storage, Display, Color, Processor, Battery,Camera

class Smartphone(models.Model):
    type = models.CharField(max_length=255)
    released_year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    more_description = models.TextField()

    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    sotorage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    processor = models.ForeignKey(Processor,on_delete=models.CASCADE)
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return self.type