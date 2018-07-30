from rest_framework import viewsets
from core.models import Spot
from core.api.serializers import SpotSerializer

class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all().order_by('-id')
    serializer_class = SpotSerializer