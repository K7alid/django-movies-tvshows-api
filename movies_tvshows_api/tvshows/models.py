from django.db import models

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=50)
    rating = models.CharField(max_length=10, blank=True, default='')
    votes = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    genre = models.CharField(max_length=255)
    stars = models.TextField()
    short_story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-rating', 'title']

    def __str__(self):
        return f"{self.title} ({self.year})"
