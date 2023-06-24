from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    privacy_preference = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        f"{self.owner}'s profile"
