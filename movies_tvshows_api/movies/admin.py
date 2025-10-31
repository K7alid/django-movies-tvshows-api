from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'genre', 'imdb_rating', 'created_at']
    list_filter = ['year', 'genre']
    search_fields = ['title', 'director', 'actors', 'imdb_id']
    ordering = ['-year', 'title']
    readonly_fields = ['created_at', 'updated_at']


