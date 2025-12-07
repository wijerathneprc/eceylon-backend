from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView   
from .models import Smartphone, SmartphoneConfig
from .serializers import SmartphoneSerializer, SmartphoneConfigSerializer


class SmartphoneListCreateView(ListAPIView, CreateAPIView):
    
    serializer_class = SmartphoneSerializer
    
    def get_queryset(self):
        queryset = Smartphone.objects.all()
        print("Serializer errors:")
        print(self.serializer.errors)
        return queryset
class SmartphoneDetailView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
class SmartphoneConfigListCreateView(ListAPIView, CreateAPIView):
    queryset = SmartphoneConfig.objects.all()
    serializer_class = SmartphoneConfigSerializer
class SmartphoneConfigDetailView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = SmartphoneConfig.objects.all()
    serializer_class = SmartphoneConfigSerializer

class SmartphoneByProductView(ListAPIView):
    serializer_class = SmartphoneSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Smartphone.objects.filter(product__id=product_id)    



