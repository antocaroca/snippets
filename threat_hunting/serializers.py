from rest_framework import serializers
from .models import Hallazgo
from django.contrib.auth.models import User

class HallazgoSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Hallazgo
        fields = ['url', 'id', 
                 'codigo', 'nombre_caso', 'criticidad', 'estado_actual', 'fecha_ultima_retroalimentacion', 'mes', 'año']