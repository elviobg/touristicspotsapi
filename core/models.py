from django.db import models
from attraction.models import Attraction
from comments.models import Comment
from reviews.models import Review
from localization.models import Localization

class Spot(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField()
  approved = models.BooleanField(default=False)
  attractions = models.ManyToManyField(Attraction)
  comments = models.ManyToManyField(Comment)
  review = models.ManyToManyField(Review)
  localization = models.ForeignKey(Localization, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
