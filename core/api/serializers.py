from rest_framework.serializers import ModelSerializer
from core.models import Spot
from attraction.api.serializers import AttractionSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer
from localization.api.serializers import LocalizationSerializer


class SpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    comments = CommentSerializer(many=True)
    review = ReviewSerializer(many=True)
    localization = LocalizationSerializer()
    
    class Meta:
        model = Spot
        fields = '__all__'
