from .models import Amenazas_Del_Mes, Alerta_Amenaza, Grafico_Lineas_Tendencia_Amenazas, Tendencia_Amenaza
from .serializers import Amenazas_Del_MesSerializer, Alerta_AmenazaSerializer, Grafico_Lineas_Tendencia_AmenazasSerializer, Tendencia_AmenazaSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers
from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from gestion_de_amenazas.forms import Amenazas_Del_MesForm, Alerta_AmenazaForm, Tendencia_AmenazaForm, Grafico_Lineas_Tendencia_AmenazasForm

from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

#############################################################################################
###################                       ViewSets                     ######################
#############################################################################################


class Amenazas_Del_MesViewSet(viewsets.ModelViewSet):
    """
    This viewset called Amenazas del mes (gestión de Amenazas) automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Amenazas_Del_Mes.objects.all()
    serializer_class = Amenazas_Del_MesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Alerta_AmenazaViewSet(viewsets.ModelViewSet):
    """
    This viewset called  alerta amenaza(gestión de Amenazas) automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Alerta_Amenaza.objects.all()
    serializer_class = Alerta_AmenazaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Grafico_Lineas_Tendencia_AmenazasViewSet(viewsets.ModelViewSet):
    """
    This viewset called Grafico_Lineas_Tendencia_Amenazas (gestión de Amenazas) automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Grafico_Lineas_Tendencia_Amenazas.objects.all()
    serializer_class = Grafico_Lineas_Tendencia_AmenazasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Tendencia_AmenazaViewSet(viewsets.ModelViewSet):
    """
    This viewset called Tendencia_Amenaza (gestión de Amenazas) automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Tendencia_Amenaza.objects.all()
    serializer_class = Tendencia_AmenazaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

#############################################################################################
###################                       Views                        ######################
#############################################################################################

####################### Amenazas_Del_Mes ##################################

class Amenazas_Del_MesCreateView(CreateView):
    model = Amenazas_Del_Mes
    template_name = "crear_amenazas_del_mes.html"
    form_class = Amenazas_Del_MesForm
    success_url = reverse_lazy('amenazas_del_mes')

    def form_valid(self, form):
        return super().form_valid(form)

class Amenazas_Del_MesUpdateView(UpdateView):
    model = Amenazas_Del_Mes
    fields = ('categoria', 'criticidad', 'tipo', 'cantidad', 'mes', 'año', 'owner')
    template_name = 'editar_amenazas_del_mes.html'

    def form_valid(self, form):
        return super().form_valid(form)

class Amenazas_Del_MesDeleteView(DeleteView):
    model = Amenazas_Del_Mes
    template_name = "eliminar_amenazas_del_mes.html"
    success_url = reverse_lazy('amenazas_del_mes')

class Amenazas_Del_MesListView(ListView):
    model = Amenazas_Del_Mes
    template_name = 'listar_amenazas_del_mes.html'
    
    """
    This view method provides the context to list the objects of
    Amenazas_Del_Mes, Alerta_Amenaza, Tendencia_Amenaza
    """

    def get_context_data(self, **kwargs):
        context = super(Amenazas_Del_MesListView, self).get_context_data(**kwargs)
        context['amenazas_del_mes'] = Amenazas_Del_Mes.objects.all()  
        context['alerta_amenazas'] = Alerta_Amenaza.objects.all() 
        context['tendencia_amenaza'] = Tendencia_Amenaza.objects.all()  
        context['grafico_tendencia'] = Grafico_Lineas_Tendencia_Amenazas.objects.all()  

        return context

###########################  Alerta_Amenaza  ######################################

class Alerta_AmenazaCreateView(CreateView):
    model = Alerta_Amenaza
    template_name = "crear_alerta_amenaza.html"
    form_class = Alerta_AmenazaForm
    success_url = reverse_lazy('amenazas_del_mes')

    def form_valid(self, form):
        return super().form_valid(form)

class Alerta_AmenazaUpdateView(UpdateView):
    model = Alerta_Amenaza
    fields = ('categoria', 'criticidad', 'descripcion', 'icono', 'mes', 'año', 'owner')
    template_name = 'editar_alerta_amenaza.html'

    def form_valid(self, form):
        return super().form_valid(form)

class Alerta_AmenazaDeleteView(DeleteView):
    model = Alerta_Amenaza
    template_name = "eliminar_alerta_amenaza.html"
    success_url = reverse_lazy('amenazas_del_mes')

###########################  Tendencia_Amenaza  ######################################

class Tendencia_AmenazaCreateView(CreateView):
    model = Tendencia_Amenaza
    template_name = "crear_tendencia_amenaza.html"
    form_class = Tendencia_AmenazaForm
    success_url = reverse_lazy('amenazas_del_mes')

    def form_valid(self, form):
        return super().form_valid(form)

class Tendencia_AmenazaUpdateView(UpdateView):
    model = Tendencia_Amenaza
    fields = ('titulo', 'descripcion_1', 'descripcion_2', 'descripcion_3', 'imagen_1', 'imagen_2', 'imagen_3', 'mes', 'año', 'owner')
    template_name = 'editar_tendencia_amenaza.html'

    def form_valid(self, form):
        return super().form_valid(form)

class Tendencia_AmenazaDeleteView(DeleteView):
    model = Tendencia_Amenaza
    template_name = "eliminar_tendencia_amenaza.html"
    success_url = reverse_lazy('amenazas_del_mes')

###########################  Grafico_Lineas_Tendencia_Amenazas  #############################

class Grafico_Lineas_Tendencia_AmenazasCreateView(CreateView):
    model = Grafico_Lineas_Tendencia_Amenazas
    template_name = "crear_grafico_lineas_tendencia_amenaza.html"
    form_class = Grafico_Lineas_Tendencia_AmenazasForm
    success_url = reverse_lazy('amenazas_del_mes')

    def form_valid(self, form):
        return super().form_valid(form)

class Grafico_Lineas_Tendencia_AmenazasUpdateView(UpdateView):
    model = Grafico_Lineas_Tendencia_Amenazas
    fields = ('titulo', 'escala', 'indicador', 'puntos', 'mes', 'año', 'owner')
    template_name = 'editar_grafico_lineas_tendencia_amenaza.html'

    def form_valid(self, form):
        return super().form_valid(form)

class Grafico_Lineas_Tendencia_AmenazasDeleteView(DeleteView):
    model = Grafico_Lineas_Tendencia_Amenazas
    template_name = "eliminar_grafico_lineas_tendencia_amenaza.html"
    success_url = reverse_lazy('amenazas_del_mes')