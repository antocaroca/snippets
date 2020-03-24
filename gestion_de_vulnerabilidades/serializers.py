from rest_framework import serializers
from .models import Vulnerabilidad
from django.contrib.auth.models import User

class VulnerabilidadSerializer(serializers.HyperlinkedModelSerializer):
    
   
    class Meta:
        model = Vulnerabilidad
        fields = ['url', 'id', 
                'fecha_inicio', 'fecha_fin', 'tipo_escaner',
                'direcciones_ip_declaradas', 'direcciones_ip_con_respuesta', 
                'direcciones_ip_sin_respuesta', 'cantidad_nivel_4', 'cantidad_nivel_3',
                'evolucion_fecha_1', 'evolucion_fecha_2', 'evolucion_criticas_1',
                'evolucion_criticas_2', 'evolucion_altas_1', 'evolucion_altas_2', 
                'evolucion_medias_1', 'evolucion_medias_2', 'evolucion_bajas_1',
                'evolucion_bajas_2', 'estado_nuevas', 'estado_no_detectadas',
                'estado_persistentes']