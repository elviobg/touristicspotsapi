from rest_framework import viewsets
from touristic_spots.comments.models import Comment
from touristic_spots.comments.api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
