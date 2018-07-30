from rest_framework.serializers import ModelSerializer
from attraction.models import Attraction

class AttractionSerializer(ModelSerializer):
  class Meta:
    model = Attraction
    fields = '__all__'