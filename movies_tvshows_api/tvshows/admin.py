from django.contrib import admin
from .models import TVShow

@admin.register(TVShow)
class TVShowAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'rating', 'genre', 'created_at']
    list_filter = ['year', 'genre']
    search_fields = ['title', 'stars', 'short_story']
    ordering = ['-rating', 'title']
    readonly_fields = ['created_at', 'updated_at']
