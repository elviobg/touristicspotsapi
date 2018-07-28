from django.db import models
from attraction.models import Attraction

class Spot(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField()
  approved = models.BooleanField(default=False)
  attractions = models.ManyToManyField(Attraction)

  def __str__(self):
    return self.name
