from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from tipo.models import Tipo
from tipo.api.serializers import TipoSerializer
from tipo.api.permissions import IsAdminOrReadOnly


class TipoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = TipoSerializer
    queryset = Tipo.objects.all()
    queryset = Tipo.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']
