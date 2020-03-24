from django.db import models
from django.forms import ModelForm
from django.urls import reverse

CRITICIDAD_AMENAZAS = (
    ("Crítico", "Crítico"), 
    ("Alto", "Alto"), 
    ("Medio", "Medio"), 
    ("Bajo", "Bajo"),  
    ("Informacional", "Informacional"),   
)

ESTADO_ACTUAL_HALLAZGO = (
    ("Vigente", "Vigente"), 
    ("Caduco", "Caduco"), 
)

MES = (
    ("Enero", "Enero"), 
    ("Febrero", "Febrero"), 
    ("Marzo", "Marzo"), 
    ("Abril", "Abril"), 
    ("Mayo", "Mayo"), 
    ("Junio", "Junio"), 
    ("Julio", "Julio"), 
    ("Agosto", "Agosto"), 
    ("Septimbre", "Septimbre"), 
    ("Octubre", "Octubre"), 
    ("Noviembre", "Noviembre"), 
    ("Diciembre", "Diciembre"), 
)

class Hallazgo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=100)
    nombre_caso = models.CharField(max_length=100)
    criticidad = models.CharField(choices=CRITICIDAD_AMENAZAS, max_length=100, default='Crítico')
    estado_actual =  models.CharField(choices=ESTADO_ACTUAL_HALLAZGO, max_length=100, default='Vigente')
    fecha_ultima_retroalimentacion = models.DateField()
    mes = models.CharField(choices=MES, max_length=100)
    año = models.PositiveSmallIntegerField(blank=True, null=True)
    

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        
        super(Hallazgo, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_caso
  
    def get_absolute_url(self):
        return reverse('hallazgo_listar')
