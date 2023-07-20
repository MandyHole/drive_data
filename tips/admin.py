from django.contrib import admin
from .models import Tip
# Register your models here.

@admin.register(Tip)
class TipsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category', 
        'owner'
        )
    ordering = ['title']