from django.db import models

class Localization(models.Model):
  line1 = models.CharField(max_length=128)
  line2 = models.CharField(max_length=128, null=True, blank=True)
  city = models.CharField(max_length=128)
  state = models.CharField(max_length=128)
  country = models.CharField(max_length=128)
  latitude = models.IntegerField(null=True, blank=True)
  langitude = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return self.line1