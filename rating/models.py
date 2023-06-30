from django.db import models
from django.contrib.auth.models import User
from tips.models import Tip

# Create your models here.
class Rating(models.Model):
    RATING_OPTIONS = [
        ('U', 'Unrated'),
        ('1', 'Very bad'),
        ('2', 'Not great'),
        ('3', 'Okay'),
        ('4', 'Quite useful'),
        ('5', 'Very useful'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tip = models.ForeignKey(
        Tip, 
        related_name="rating",
        on_delete=models.CASCADE)
    tip_rating = models.CharField(
        choices=RATING_OPTIONS,
        max_length=30,
        default='Unrated',
        verbose_name="Rate this tip")

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'tip']


    def __str__(self):
        return f"{self.owner}'s rating for {self.tip}: {self.rating}"