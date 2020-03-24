from django import forms
from threat_hunting.models import Hallazgo

class HallazgoForm(forms.ModelForm):
    
    class Meta: 
        model =  Hallazgo
        fields = ('codigo', 'nombre_caso', 'criticidad', 'estado_actual', 'fecha_ultima_retroalimentacion', 'mes', 'año')