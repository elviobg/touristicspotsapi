from django.db import models
from touristic_spots.attraction.models import Attraction
from touristic_spots.comments.models import Comment
from touristic_spots.reviews.models import Review
from touristic_spots.localization.models import Localization


class Spot(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction, null=True, blank=True)
    comments = models.ManyToManyField(Comment, null=True, blank=True)
    review = models.ManyToManyField(Review, null=True, blank=True)
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE,
                                     null=True, blank=True)
    image = models.ImageField(upload_to='spots', null=True, blank=True)

    def __str__(self):
        return self.name
