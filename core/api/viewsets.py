from rest_framework import viewsets
from core.models import Spot
from core.api.serializers import SpotSerializer

class SpotViewSet(viewsets.ModelViewSet):
    #queryset = Spot.objects.all().order_by('-id')
    serializer_class = SpotSerializer

    def get_queryset(self):
      return Spot.objects.all().filter(approved=True)

    #método de sobrescrita das chamadas padrão
    #list, create, destroy, retrieve, update, partial_update
    def list(self, request, *args, **kwargs):
      return super(SpotViewSet, self).list(request, *args, **kwargs)
  