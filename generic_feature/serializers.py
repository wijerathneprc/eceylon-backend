from rest_framework.serializers import ModelSerializer
from .models import Ram, Storage, OperatingSystem, Display, Processor, SimCard, Battery,GrapichCard, Color, Connectivity, Camera



class RamSerializer(ModelSerializer):
    
    class Meta:
        model = Ram
        fields ='__all__'
    


class StorageSerializer(ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class DisplaySerializer(ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class ProcessorSerializer(ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'

class OperatingSystemSerializer(ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = '__all__'

class GrapichCardSerializer(ModelSerializer):
    class Meta:
        model = GrapichCard
        fields = '__all__'

class ConnectivitySerializer(ModelSerializer):
    class Meta:
        model = Connectivity
        fields = '__all__'

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class CameraSerializer(ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

class BatterySerializer(ModelSerializer):
    class Meta:
        model = Battery
        fields = '__all__'

class SimCardSerializer(ModelSerializer):
    class Meta:
        model = SimCard
        fields = '__all__'
