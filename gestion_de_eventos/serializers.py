from rest_framework import serializers
from .models import Eventos_Del_Mes, Data_Source
from django.contrib.auth.models import User

class Eventos_Del_MesSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Eventos_Del_Mes
        fields = ['url', 'id', 
                 'evento_n1', 'evento_n2', 'evento_n3', 'evento_pro', 'mes', 'año', 'evento_gestionado', 'evento_no_gestionado']

class Data_SourceSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Data_Source
        fields = ['url', 'id', 
                  'nombre', 'estado', 'ip', 'mes', 'año']