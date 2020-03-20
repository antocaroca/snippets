from django.contrib import admin
from .models import Amenazas_Del_Mes, Alerta_Amenaza, Grafico_Lineas_Tendencia_Amenazas, Tendencia_Amenaza


admin.site.register(Amenazas_Del_Mes)
admin.site.register(Alerta_Amenaza)
admin.site.register(Grafico_Lineas_Tendencia_Amenazas)
admin.site.register(Tendencia_Amenaza)