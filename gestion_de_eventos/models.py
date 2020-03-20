from django.db import models
from django.forms import ModelForm
from pygments.formatters.html import HtmlFormatter
from django.urls import reverse

ESTADO_AMENAZAS = (
    ("Integrado", "Integrado"), 
    ("Modificado", "Modificado"), 
    ("Eliminado", "Eliminado"), 
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

class Eventos_Del_Mes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    evento_n1 = models.PositiveIntegerField(blank=True, null=True)
    evento_n2 = models.PositiveIntegerField(blank=True, null=True)
    evento_n3 = models.PositiveIntegerField(blank=True, null=True)
    evento_pro = models.PositiveIntegerField(blank=True, null=True)
    mes = models.CharField(choices=MES, max_length=100)
    año = models.PositiveSmallIntegerField(blank=True, null=True)
    evento_gestionado = models.PositiveIntegerField(blank=True, null=True)
    evento_no_gestionado = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='eventos_del_mes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        verbose_name = 'Eventos Del Mes'
        verbose_name_plural = 'Eventos Del Mes'

    def save(self, *args, **kwargs):
        super(Eventos_Del_Mes, self).save(*args, **kwargs)

    def __str__(self):
        return self.mes
  
    def get_absolute_url(self):
        return reverse('eventos_del_mes')

class Data_Source(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(choices=ESTADO_AMENAZAS, max_length=100, default='Integrado')
    ip = models.GenericIPAddressField(blank=True, null=True)
    mes = models.CharField(choices=MES, max_length=100)
    año = models.PositiveSmallIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='data_source', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        
        super(Data_Source, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
        
    def get_absolute_url(self):
        return reverse('eventos_del_mes')