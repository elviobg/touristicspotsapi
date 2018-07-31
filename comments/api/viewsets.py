from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'description',)
