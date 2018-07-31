from django.db import models
from attraction.models import Attraction
from comments.models import Comment
from reviews.models import Review
from localization.models import Localization

class Spot(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField()
  approved = models.BooleanField(default=False)
  attractions = models.ManyToManyField(Attraction, null=True, blank=True)
  comments = models.ManyToManyField(Comment, null=True, blank=True)
  review = models.ManyToManyField(Review, null=True, blank=True)
  localization = models.ForeignKey(Localization, on_delete=models.CASCADE, null=True, blank=True)
  image = models.ImageField(upload_to='spots', null=True, blank=True)

  def __str__(self):
    return self.name
