from django.db import models
from pygments.formatters.html import HtmlFormatter

CATEGORIA_AMENAZAS = (
    ("Gestionadas", "Gestionadas"), 
    ("No Gestionadas", "No Gestionadas"),   
)

CRITICIDAD_AMENAZAS = (
    ("Crítico", "Crítico"), 
    ("Alto", "Alto"), 
    ("Medio", "Medio"), 
    ("Bajo", "Bajo"),  
    ("Informacional", "Informacional"),   
)

TIPO_AMENAZAS = (
    ("Malware", "Malware"), 
    ("Vulnerabilidad", "Vulnerabilidad"),  
    ("Parche", "Parche"), 
    ("APT", "APT"),  
    ("Phishing", "Phishing"),  
)

class Amenazas_Del_Mes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(choices=CATEGORIA_AMENAZAS, max_length=100, default='Gestionadas')
    criticidad = models.CharField(choices=CRITICIDAD_AMENAZAS, max_length=100, default='Crítico')
    tipo = models.CharField(choices=TIPO_AMENAZAS, max_length=100, default='Malware')
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='amenazas_del_mes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        
        super(Amenazas_Del_Mes, self).save(*args, **kwargs)

class Alerta_Amenaza(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(choices=CATEGORIA_AMENAZAS, max_length=100, default='Gestionadas')
    criticidad = models.CharField(choices=CRITICIDAD_AMENAZAS, max_length=100, default='Crítico')
    descripcion = models.TextField(blank=True, null=True)
    icono =  models.ImageField(upload_to='gestion_de_amenazas/alerta_amenaza/', null=True, blank=True)
    mes = models.PositiveIntegerField(blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='alerta_amenaza', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        super(Alerta_Amenaza, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.icono.delete()
        super().delete(*args, **kwargs)

class Tendencia_Amenaza(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    descripcion_1 = models.TextField(blank=True, null=True)
    descripcion_2 = models.TextField(blank=True, null=True)
    descripcion_3 = models.TextField(blank=True, null=True)
    imagen_1 =  models.ImageField(upload_to='gestion_de_amenazas/tendencia_amenaza/', null=True, blank=True)
    imagen_2 =  models.ImageField(upload_to='gestion_de_amenazas/tendencia_amenaza/', null=True, blank=True)
    imagen_3 =  models.ImageField(upload_to='gestion_de_amenazas/tendencia_amenaza/', null=True, blank=True)
    mes = models.PositiveIntegerField(blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='tendencia_Amenaza', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        super(Tendencia_Amenaza, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.imagen_1.delete()
        self.imagen_2.delete()
        self.imagen_3.delete()
        super().delete(*args, **kwargs)

class Grafico_Lineas_Tendencia_Amenazas(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    escala = models.PositiveIntegerField(blank=True, null=True)
    indicador = models.CharField(max_length=100, blank=True, null=True)
    puntos = models.PositiveIntegerField(blank=True, null=True)
    mes = models.PositiveIntegerField(blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='Grafico_lineas_tendencia_amenazas', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        super(Grafico_Lineas_Tendencia_Amenazas, self).save(*args, **kwargs)
