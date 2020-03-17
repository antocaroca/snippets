from django.db import models
from pygments.formatters.html import HtmlFormatter

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

class Hallazgo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=100)
    nombre_caso = models.CharField(max_length=100)
    criticidad = models.CharField(choices=CRITICIDAD_AMENAZAS, max_length=100, default='Crítico')
    estado_actual =  models.CharField(choices=ESTADO_ACTUAL_HALLAZGO, max_length=100, default='Vigente')
    fecha_ultima_retroalimentacion = models.DateField()
    mes = models.PositiveIntegerField(blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='hallazgo', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        
        super(Hallazgo, self).save(*args, **kwargs)

