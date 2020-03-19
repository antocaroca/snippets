from django import forms
from gestion_de_amenazas.models import Amenazas_Del_Mes, Alerta_Amenaza, Tendencia_Amenaza, Grafico_Lineas_Tendencia_Amenazas

class Amenazas_Del_MesForm(forms.ModelForm):
    
    class Meta: 
        model =  Amenazas_Del_Mes
        fields = ('categoria', 'criticidad', 'tipo', 'cantidad', 'mes', 'año' ,'owner')

class Alerta_AmenazaForm(forms.ModelForm):
    
    class Meta: 
        model =  Alerta_Amenaza
        fields = ('categoria', 'criticidad', 'descripcion', 'icono', 'mes', 'año' ,'owner', )

class Tendencia_AmenazaForm(forms.ModelForm):
    
    class Meta: 
        model =  Tendencia_Amenaza
        fields = ('titulo', 'descripcion_1', 'descripcion_2', 'descripcion_3', 'imagen_1', 'imagen_2', 'imagen_3', 'mes', 'año' ,'owner', )

class Grafico_Lineas_Tendencia_AmenazasForm(forms.ModelForm):
    
    class Meta: 
        model =  Grafico_Lineas_Tendencia_Amenazas
        fields = ('titulo', 'escala', 'indicador', 'puntos', 'mes', 'año' ,'owner')