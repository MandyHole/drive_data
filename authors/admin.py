from django.contrib import admin
from .models import TipAuthor

# admin.site.register(TipAuthor)

# Register your models here.


@admin.register(TipAuthor)
class TipAuthorAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'name',
        'bio'
    )
    ordering = ['name']