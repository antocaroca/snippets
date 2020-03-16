from django.db import models
from pygments.formatters.html import HtmlFormatter

ESTADO_AMENAZAS = (
    ("Integrado", "Integrado"), 
    ("Modificado", "Modificado"), 
    ("Eliminado", "Eliminado"), 
)

class Eventos_Del_Mes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    evento_n1 = models.PositiveIntegerField(blank=True, null=True)
    evento_n2 = models.PositiveIntegerField(blank=True, null=True)
    evento_n3 = models.PositiveIntegerField(blank=True, null=True)
    evento_pro = models.PositiveIntegerField(blank=True, null=True)
    mes = models.PositiveIntegerField(blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    evento_gestionado = models.PositiveIntegerField(blank=True, null=True)
    evento_no_gestionado = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='eventos_del_mes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        
        super(Eventos_Del_Mes, self).save(*args, **kwargs)

class Data_Source(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(choices=ESTADO_AMENAZAS, max_length=100, default='Integrado')
    ip = models.CharField(max_length=100, blank=True, null=True)
    mes = models.PositiveIntegerField(blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='data_source', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        
        super(Data_Source, self).save(*args, **kwargs)