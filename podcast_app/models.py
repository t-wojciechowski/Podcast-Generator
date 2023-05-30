from django.db import models

# Create your models here.

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
