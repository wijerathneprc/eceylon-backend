from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets, generics

from .serializers import RamSerializer, StorageSerializer, ColorSerializer, SimCardSerializer, BatterySerializer, GrapichCardSerializer
from .models import Ram, Storage, Color, Battery, SimCard, GrapichCard

class RamCreateView(generics.CreateAPIView):

    queryset = Ram.objects.all()
    serializer_class = RamSerializer
    
class RamListView(generics.ListAPIView):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer
    
    
class StorageCreateView(generics.CreateAPIView):

    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    
class ColorListView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    
    
class ColorCreateView(generics.CreateAPIView):

    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    
    
class BatteryCreateView(generics.CreateAPIView):

    queryset = Battery.objects.all()
    serializer_class = BatterySerializer
    
    
class SimCardCreateView(generics.CreateAPIView):

    queryset = SimCard.objects.all()
    serializer_class = SimCardSerializer
    
    
class GraphicCardCreateView(generics.CreateAPIView):

    queryset = GrapichCard.objects.all()
    serializer_class = GrapichCardSerializer