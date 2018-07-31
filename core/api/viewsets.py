from rest_framework import viewsets
from core.models import Spot
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import SpotSerializer


class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'description', )

    def get_queryset(self):
        return Spot.objects.all().filter(approved=True)

    # método de sobrescrita das chamadas padrão
    # list, create, destroy, retrieve, update, partial_update
    def list(self, request, *args, **kwargs):
        return super(SpotViewSet, self).list(request, *args, **kwargs)
