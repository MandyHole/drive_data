from django.db import models
from django.contrib.auth.models import User
from tips.models import Tip

# Create your models here.


class Comment(models.Model):
    """
    Comment Model
    Relates to Tip and User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
