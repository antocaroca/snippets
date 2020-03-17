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