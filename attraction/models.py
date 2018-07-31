from django.db import models

class Attraction(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField()
  operation_time = models.TextField()
  minimal_age = models.IntegerField()
  image = models.ImageField(upload_to='attractions', null=True, blank=True)

  def __str__(self):
    return self.name