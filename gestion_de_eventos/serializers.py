from rest_framework import serializers
from .models import Eventos_Del_Mes
from django.contrib.auth.models import User

class Eventos_Del_MesSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   

    class Meta:
        model = Eventos_Del_Mes
        fields = ['url', 'id', 'owner',
                 'evento_n1', 'evento_n2', 'evento_n3', 'evento_pro', 'mes', 'año', 'evento_gestionado', 'evento_no_gestionado']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']