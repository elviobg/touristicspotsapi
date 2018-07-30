from rest_framework import viewsets
from localization.models import Localization
from localization.api.serializers import LocalizationSerializer

class LocalizationViewSet(viewsets.ModelViewSet):
    queryset = Localization.objects.all().order_by('-id')
    serializer_class = LocalizationSerializer