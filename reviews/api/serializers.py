from rest_framework.serializers import ModelSerializer
from touristic_spots.reviews.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
