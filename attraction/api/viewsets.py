from rest_framework import viewsets
from attraction.models import Attraction
from attraction.api.serializers import AttractionSerializer


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all().order_by('-id')
    serializer_class = AttractionSerializer
