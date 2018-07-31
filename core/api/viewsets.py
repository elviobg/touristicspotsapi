from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Spot
from .serializers import SpotSerializer


class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )
    filter_fields = ('name', 'description', )
    
    def get_queryset(self):
        return Spot.objects.all().filter(approved=True)

    # método de sobrescrita das chamadas padrão
    # list, create, destroy, retrieve, update, partial_update
    def list(self, request, *args, **kwargs):
        return super(SpotViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(SpotViewSet, self).retrieve(request, *args, **kwargs)