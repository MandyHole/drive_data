from django.db import models
from django.contrib.auth.models import User
from tips.models import Tip


# Create your models here.
class SavedTip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tip = models.ForeignKey(
        Tip,
        related_name="author_saved_tip",
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'tip']

    def __str__(self):
        return f"{self.owner} saved {self.tip}"
