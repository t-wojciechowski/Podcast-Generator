from django.db import models

# Create your models here.

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, default='Unknown')
    description = models.TextField()


    def __str__(self):
        return f'{self.title}, by {self.author} {self.description}'



