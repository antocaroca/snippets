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