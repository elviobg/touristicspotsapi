from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from reviews.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'description',)
