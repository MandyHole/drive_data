from django.contrib import admin
from .models import Author

# admin.site.register(Author)

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'name',
        'bio'
    )
    ordering = ['name']
