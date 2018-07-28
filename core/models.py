from django.db import models

class Spot(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField()
  approved = models.BooleanField(default=False)

  def __str__(self):
    return self.name
