
from rest_framework import serializers
from .models import TrMbship, UrMbship

class TrMbshipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrMbship
        fields = '__all__'

class UrMbshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrMbship
        fields = '__all__'
