from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from localization.models import Localization
from .serializers import LocalizationSerializer


class LocalizationViewSet(viewsets.ModelViewSet):
    queryset = Localization.objects.all().order_by('-id')
    serializer_class = LocalizationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'description',)
