from rest_framework import viewsets
from touristic_spots.reviews.models import Review
from touristic_spots.reviews.api.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
