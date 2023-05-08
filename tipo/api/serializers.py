from rest_framework import serializers
from tipo.models import Tipo

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = []
