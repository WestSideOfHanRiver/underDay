# backend/post/serializers.py
from rest_framework import serializers
from .models import UrMaster

class UrMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrMaster
        fields = '__all__'

