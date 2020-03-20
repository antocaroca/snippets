from .models import Hallazgo
from .serializers import HallazgoSerializer
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

from threat_hunting.forms import HallazgoForm

from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

###################################    ViewSet   #####################################

class HallazgoViewSet(viewsets.ModelViewSet):
    """
    This viewset called  Hallazgo (threat hunting) automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Hallazgo.objects.all()
    serializer_class = HallazgoSerializer
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

###################################    views    #####################################

class HallazgoCreateView(CreateView):
    model = Hallazgo
    template_name = "crear_hallazgo.html"
    form_class = HallazgoForm
    success_url = reverse_lazy('hallazgo_listar')

    def form_valid(self, form):
        return super().form_valid(form)

class HallazgoUpdateView(UpdateView):
    model = Hallazgo
    fields = ('codigo', 'nombre_caso', 'criticidad', 'estado_actual', 'fecha_ultima_retroalimentacion', 'mes', 'año', 'owner')
    template_name = 'editar_hallazgo.html'

    def form_valid(self, form):
        return super().form_valid(form)

class HallazgoDeleteView(DeleteView):
    model = Hallazgo
    template_name = "eliminar_hallazgo.html"
    success_url = reverse_lazy('hallazgo_listar')

class HallazgoListView(ListView):
    model = Hallazgo
    template_name = 'hallazgo_listar.html'
    context_object_name = 'lista_hallazgo'