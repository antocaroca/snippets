from django import forms
from gestion_de_vulnerabilidades.models import Vulnerabilidad

class VulnerabilidadForm(forms.ModelForm):
    cantidad_nivel_4 = forms.IntegerField(min_value=0) 
    cantidad_nivel_3 = forms.IntegerField(min_value=0) 
    evolucion_criticas_1 = forms.IntegerField(min_value=0) 
    
    class Meta: 
        model =  Vulnerabilidad
        fields = (
                'fecha_inicio', 'fecha_fin', 'tipo_escaner',
                'direcciones_ip_declaradas', 'direcciones_ip_con_respuesta', 
                'direcciones_ip_sin_respuesta', 'cantidad_nivel_4', 'cantidad_nivel_3',
                'evolucion_fecha_1', 'evolucion_fecha_2', 'evolucion_criticas_1',
                'evolucion_criticas_2', 'evolucion_altas_1', 'evolucion_altas_2', 
                'evolucion_medias_1', 'evolucion_medias_2', 'evolucion_bajas_1',
                'evolucion_bajas_2', 'estado_nuevas', 'estado_no_detectadas',
                'estado_persistentes', 'owner'
                )