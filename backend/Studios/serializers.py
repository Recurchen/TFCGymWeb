from email.mime import image
from rest_framework import serializers

from .models import Studio, Image, Amenity



class StudioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['name', 'image', 'studio']

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['type', 'quantity', 'studio']

class StudioSerializer(serializers.ModelSerializer):
    amenities = AmenitySerializer(many = True)
    images = StudioImageSerializer(many = True)
    class Meta:
        model = Studio
        fields = ['id', 'name', 'address', 'postal_code', 'phone_number',
        'longitude', 'latitude',
         'amenities', 'images']

class UserLocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    location = serializers.CharField(max_length = 255)
<<<<<<< HEAD
    amenities = serializers.CharField(max_length = 255)

=======
>>>>>>> 2a2cd131ab18be77d78d7d87195a421d721850a4
