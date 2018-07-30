from rest_framework.serializers import ModelSerializer
from core.models import Spot

class SpotSerializer(ModelSerializer):
  class Meta:
    model = Spot
    fields = '__all__'