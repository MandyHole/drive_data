from django.db import models
from django.contrib.auth.models import User
from tips.models import Tip

# Create your models here.


class Rating(models.Model):
    """
    Rate a tip on how useful it is.
    Only one rating per author/tip
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tip = models.ForeignKey(
        Tip,
        related_name="rating",
        on_delete=models.CASCADE)
    tip_rating = models.IntegerField()

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'tip']

    def __str__(self):
        return f"{self.owner}'s rating for {self.tip}: {self.rating}"
