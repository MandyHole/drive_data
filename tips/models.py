from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tip(models.Model):
    ABILITY_LEVEL = [
        ('beginner', 'Beginner+'),
        ('intermediate', 'Intermediate+'),
        ('advanced', 'Advanced'),
    ]
    TIP_CATEGORY = [
        ('drive_pdf', 'Drive/PDFs'),
        ('sheets', 'Sheets'),
        ('slides', 'Slides'),
        ('docs', 'Docs'),
        ('forms', 'Forms'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    tip_content = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    screenshot = models.ImageField(
        upload_to='GetDriveing/',
        verbose_name="Upload a screenshot if applicable",
        default='../screenshot-default_gbgobl.jpg',
        blank=True)
    category = models.CharField(
        max_length=32,
        choices=TIP_CATEGORY,
        blank=False,
        verbose_name="Primary category of tip"
        )
    ability = models.CharField(
        max_length=32,
        blank=False,
        choices=ABILITY_LEVEL,
        verbose_name="Recommended ability level"
        )

    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return f"{self.title}, {self.category}"
