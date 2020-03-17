from rest_framework import serializers
from .models import Amenazas_Del_Mes, Alerta_Amenaza, Grafico_Lineas_Tendencia_Amenazas, Tendencia_Amenaza
from django.contrib.auth.models import User

class Amenazas_Del_MesSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Amenazas_Del_Mes
        fields = ['url', 'id', 'owner',
                  'categoria', 'criticidad', 'tipo', 'cantidad', 'mes', 'año']

class Alerta_AmenazaSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Alerta_Amenaza
        fields = ['url', 'id', 'owner',
                  'categoria', 'criticidad', 'descripcion', 'icono', 'mes', 'año']

class Grafico_Lineas_Tendencia_AmenazasSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Grafico_Lineas_Tendencia_Amenazas
        fields = ['url', 'id', 'owner',
                  'titulo', 'escala', 'indicador', 'puntos', 'mes', 'año']

class Tendencia_AmenazaSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Tendencia_Amenaza
        fields = ['url', 'id', 'owner',
                  'titulo', 'descripcion_1', 'descripcion_2', 'descripcion_3', 'imagen_1', 'imagen_2', 'imagen_3', 'mes', 'año']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']