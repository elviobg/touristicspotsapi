from django.db import models

class Attraction(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField()
  operation_time = models.TextField()
  minimal_age = models.IntegerField()

  def __str__(self):
    return self.name