from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  approved = models.BooleanField(default=False)

  def __str__(self):
    return self.user.first_name