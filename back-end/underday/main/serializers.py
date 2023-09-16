
from rest_framework import serializers
from .models import UrMaster,TrClass,TrMbship

class UrMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrMaster
        fields = '__all__'

class TrClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrClass
        fields = '__all__'   

class TrMbshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrMbship
        fields = '__all__'  

