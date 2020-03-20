from django.db import models
from django.forms import ModelForm
from pygments.formatters.html import HtmlFormatter
from django.urls import reverse

TIPO_ESCANER = (
    ("Perimetral", "Perimetral"), 
    ("Interno", "Interno"), 
)

class Vulnerabilidad(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo_escaner = models.CharField(choices=TIPO_ESCANER, max_length=100, default='Perimetral')
    direcciones_ip_declaradas =  models.GenericIPAddressField()
    direcciones_ip_con_respuesta = models.GenericIPAddressField()
    direcciones_ip_sin_respuesta = models.GenericIPAddressField()
    cantidad_nivel_4 = models.PositiveIntegerField() 
    cantidad_nivel_3 = models.PositiveIntegerField() 
    evolucion_fecha_1 = models.DateField()
    evolucion_fecha_2 = models.DateField()
    evolucion_criticas_1 = models.PositiveIntegerField() 
    evolucion_criticas_2 = models.PositiveIntegerField() 
    evolucion_altas_1 = models.PositiveIntegerField() 
    evolucion_altas_2 = models.PositiveIntegerField() 
    evolucion_medias_1 = models.PositiveIntegerField() 
    evolucion_medias_2 = models.PositiveIntegerField() 
    evolucion_bajas_1 = models.PositiveIntegerField() 
    evolucion_bajas_2 = models.PositiveIntegerField() 
    estado_nuevas = models.PositiveIntegerField() 
    estado_no_detectadas = models.PositiveIntegerField() 
    estado_persistentes = models.PositiveIntegerField() 
    owner = models.ForeignKey('auth.User', related_name='vulnerabilidad', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        verbose_name = 'Vulnerabilidad'
        verbose_name_plural = 'Vulnerabilidades'

    def save(self, *args, **kwargs):
        super(Vulnerabilidad, self).save(*args, **kwargs)

    def __str__(self):
        return self.tipo_escaner
        
    def get_absolute_url(self):
        return reverse('vulnerabilidad_listar')