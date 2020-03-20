from .models import Eventos_Del_Mes, Data_Source
from .serializers import Eventos_Del_MesSerializer, Data_SourceSerializer
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

from gestion_de_eventos.forms import Eventos_Del_MesForm, Data_SourceForm

from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

#############################################################################################
###################                       ViewSets                     ######################
#############################################################################################

class Eventos_Del_MesViewSet(viewsets.ModelViewSet):
    """
    This viewset called Eventos del mes (gestión de eventos) automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Eventos_Del_Mes.objects.all()
    serializer_class = Eventos_Del_MesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Data_SourceViewSet(viewsets.ModelViewSet):
    """
    This viewset called data source (gestión de eventos) automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Data_Source.objects.all()
    serializer_class = Data_SourceSerializer
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

class Eventos_Del_MesCreateView(CreateView):
    model = Eventos_Del_Mes
    template_name = "crear_eventos_del_mes.html"
    form_class = Eventos_Del_MesForm
    success_url = reverse_lazy('eventos_del_mes')

    def form_valid(self, form):
        return super().form_valid(form)

class Eventos_Del_MesUpdateView(UpdateView):
    model = Eventos_Del_Mes
    fields = ('evento_n1', 'evento_n2', 'evento_n3', 'evento_pro',
            'mes', 'año', 'evento_gestionado', 'evento_no_gestionado', 'owner')
    template_name = 'editar_eventos_del_mes.html'

    def form_valid(self, form):
        return super().form_valid(form)

class Eventos_Del_MesDeleteView(DeleteView):
    model = Eventos_Del_Mes
    template_name = "eliminar_eventos_del_mes.html"
    success_url = reverse_lazy('eventos_del_mes')

class Eventos_Del_MesListView(ListView):
    model = Eventos_Del_Mes
    template_name = 'eventos_del_mes_listar.html'
    context_object_name = 'eventos_del_mes'

    #aca se muestra el contexto de  Eventos_Del_Mes y data_source
    def get_context_data(self, **kwargs):
        context = super(Eventos_Del_MesListView, self).get_context_data(**kwargs)
        context['eventos_del_mes'] = Eventos_Del_Mes.objects.all()  
        context['data_source'] = Data_Source.objects.all()  

        return context

####################### data source ##################################

class Data_SourceCreateView(CreateView):
    model = Data_Source
    template_name = "crear_data_source.html"
    form_class = Data_SourceForm
    success_url = reverse_lazy('eventos_del_mes')

    def form_valid(self, form):
        return super().form_valid(form)

class Data_SourceUpdateView(UpdateView):
    model = Data_Source
    fields = ( 'owner', 'nombre', 'estado', 'ip', 'mes', 'año')
    template_name = 'editar_data_source.html'

    def form_valid(self, form):
        return super().form_valid(form)

class Data_SourceDeleteView(DeleteView):
    model = Data_Source
    template_name = "eliminar_data_source.html"
    success_url = reverse_lazy('eventos_del_mes')