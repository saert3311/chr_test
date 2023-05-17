from rest_framework import serializers
from .models import Proyecto, Procedimientos

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ProcedimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimientos
        fields = '__all__'