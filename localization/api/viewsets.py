from rest_framework import viewsets
from touristic_spots.localization.models import Localization
from touristic_spots.localization.api.serializers import LocalizationSerializer


class LocalizationViewSet(viewsets.ModelViewSet):
    queryset = Localization.objects.all().order_by('-id')
    serializer_class = LocalizationSerializer
