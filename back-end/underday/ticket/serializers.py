
from rest_framework import serializers
from .models import TrMbship

class TrMbshipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrMbship
        fields = '__all__'
