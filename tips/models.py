from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tip(models.Model):
    ABILITY_LEVEL = (
        ('B', 'Beginner+'),
        ('I', 'Intermediate+'),
        ('A', 'Advanced'),
    )
    TIP_CATEGORY = (
        ('D', 'Drive/PDFs'),
        ('Sh', 'Sheets'),
        ('S', 'Slides'),
        ('D', 'Docs'),
        ('F', 'Forms'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    tip_content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    screenshot = models.ImageField(
        upload_to='GetDriveing/',
        verbose_name="Upload a screenshot if applicable",
        blank=True)
    category: models.CharField(
        max_length=2,
        default=0,
        choices=TIP_CATEGORY,
        verbose_name="Primary category of tip"
        )
    ability: models.CharField(
        max_length=1,
        default=0,
        choices=ABILITY_LEVEL,
        verbose_name="Recommended ability level"
        )
    
    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return f"{self.title}, {self.category}"