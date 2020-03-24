from .models import Vulnerabilidad
from .serializers import VulnerabilidadSerializer
from rest_framework import generics
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers
from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from gestion_de_vulnerabilidades.forms import VulnerabilidadForm

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class VulnerabilidadViewSet(viewsets.ModelViewSet):
    """
    This viewset called Vulnerabilidad (gestión de vulnerabilidades) automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Vulnerabilidad.objects.all()
    serializer_class = VulnerabilidadSerializer

    def perform_create(self, serializer):
        serializer.save()


class VulnerabilidadListView(ListView):
    model = Vulnerabilidad
    template_name = "listar_vulnerabilidad.html"
    context_object_name= 'vulnerabilidad_lista'

class VulnerabilidadCreateView(CreateView):
    model = Vulnerabilidad
    template_name = "crear_vulnerabilidad.html"
    form_class = VulnerabilidadForm
    success_url = reverse_lazy('vulnerabilidad_listar')

    def form_valid(self, form):
        return super().form_valid(form)

class VulnerabilidadDetailView(DetailView):
    model = Vulnerabilidad
    template_name = 'detalle_vulnerabilidad.html'
    context_object_name = 'vulnerabilidad'

class VulnerabilidadUpdateView(UpdateView):
    model = Vulnerabilidad
    fields = (
                'fecha_inicio', 'fecha_fin', 'tipo_escaner',
                'direcciones_ip_declaradas', 'direcciones_ip_con_respuesta', 
                'direcciones_ip_sin_respuesta', 'cantidad_nivel_4', 'cantidad_nivel_3',
                'evolucion_fecha_1', 'evolucion_fecha_2', 'evolucion_criticas_1',
                'evolucion_criticas_2', 'evolucion_altas_1', 'evolucion_altas_2', 
                'evolucion_medias_1', 'evolucion_medias_2', 'evolucion_bajas_1',
                'evolucion_bajas_2', 'estado_nuevas', 'estado_no_detectadas',
                'estado_persistentes'
                )
    template_name = 'editar_vulnerabilidad.html'

    def form_valid(self, form):
        return super().form_valid(form)

class VulnerabilidadDeleteView(DeleteView):
    model = Vulnerabilidad
    template_name = "eliminar_vulnerabilidad.html"
    success_url = reverse_lazy('vulnerabilidad_listar')