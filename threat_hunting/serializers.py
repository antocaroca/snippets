from rest_framework import serializers
from .models import Hallazgo
from django.contrib.auth.models import User

class HallazgoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Hallazgo
        fields = ['url', 'id', 'owner',
                 'codigo', 'nombre_caso', 'criticidad', 'estado_actual', 'fecha_ultima_retroalimentacion', 'mes', 'año']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']