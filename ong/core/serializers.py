from .models import Proveedor
from rest_framework import serializers

class ProveedorSerilizer(serializers.ModelSerializer):    
    class Meta:
        model = Proveedor
        fields = '__all__'
