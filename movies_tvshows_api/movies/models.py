from django.db import models

class Movie(models.Model):
    # Basic Info
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rated = models.CharField(max_length=10, blank=True)
    released = models.CharField(max_length=50, blank=True)
    runtime = models.CharField(max_length=50, blank=True)
    
    # Content Info
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    actors = models.TextField()
    plot = models.TextField()
    
    # Additional Info
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    awards = models.TextField(blank=True)
    poster = models.URLField(max_length=500)
    
    # Ratings
    metascore = models.IntegerField(null=True, blank=True)
    imdb_rating = models.CharField(max_length=10)
    imdb_votes = models.CharField(max_length=50)
    imdb_id = models.CharField(max_length=20, unique=True)
    
    # Images (نخليها JSONField عشان تخزن array)
    images = models.JSONField(default=list, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-year', 'title']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
    
    def __str__(self):
        return f"{self.title} ({self.year})"
