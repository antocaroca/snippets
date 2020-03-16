from django.db import models
from pygments.formatters.html import HtmlFormatter


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