from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    """
    Author Model
    One to One relationship with owner
    Default image supplied
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='GetDriveing/',
        default='../blank-profile-picture-gb6ded336d_640_xyxqab.png')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(owner=instance)


post_save.connect(create_author, sender=User)
