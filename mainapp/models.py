# models.py
from django.db import models

class Insight(models.Model):
    end_year = models.CharField(max_length=255, blank=True, null=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=255)
    start_year = models.CharField(max_length=255, blank=True, null=True)
    impact = models.TextField(blank=True, null=True)
    added = models.DateTimeField()
    published = models.DateTimeField()
    country = models.CharField(max_length=255)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField()

    def __str__(self):
        return self.title  # Modify based on your preference
