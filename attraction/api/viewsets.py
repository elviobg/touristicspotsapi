from rest_framework import viewsets
from touristic_spots.attraction.models import Attraction
from touristic_spots.attraction.api.serializers import AttractionSerializer


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all().order_by('-id')
    serializer_class = AttractionSerializer
