from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from attraction.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all().order_by('-id')
    serializer_class = AttractionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', )
