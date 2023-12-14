from rest_framework import serializers
from .models import Cars


# Create serializers here

class CarsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"
