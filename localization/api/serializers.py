from rest_framework.serializers import ModelSerializer
from touristic_spots.localization.models import Localization


class LocalizationSerializer(ModelSerializer):
    class Meta:
        model = Localization
        fields = '__all__'
