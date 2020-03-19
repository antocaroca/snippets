from django import forms
from gestion_de_eventos.models import Eventos_Del_Mes, Data_Source

class Eventos_Del_MesForm(forms.ModelForm):
    
    class Meta: 
        model =  Eventos_Del_Mes
        fields = ('evento_n1', 'evento_n2', 'evento_n3', 'evento_pro',
            'mes', 'año', 'evento_gestionado', 'evento_no_gestionado', 'owner')

class Data_SourceForm(forms.ModelForm):
    
    class Meta: 
        model =  Data_Source
        fields = ('owner', 'nombre', 'estado', 'ip', 'mes', 'año')