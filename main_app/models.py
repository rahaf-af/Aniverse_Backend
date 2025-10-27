from django.db import models

# Create your models here.

class Anime (models.Model):
    title = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='anime_posters/')
    genre = models.CharField(max_length=50 , default='action')
    rating =models.FloatField(default=0.0)
    description = models.TextField(default= 'No description yet', null=True , blank=True)
    def __str__(self):
        return f'{self.title}'