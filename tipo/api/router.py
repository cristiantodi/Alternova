from rest_framework.routers import DefaultRouter
from tipo.api.views import TipoSerializer

router_tipo = DefaultRouter()

router_tipo.register(prefix='tipo', basename='tipo', viewset=TipoSerializer)