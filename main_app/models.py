from django.db import models

# Create your models here.

class Anime (models.Model):
    title = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='anime_posters/', null=True , blank=True )
    genre = models.CharField(max_length=100 , default='Action')
    rating =models.FloatField(default=0.0)
    description = models.TextField(default= 'No description yet', null=True , blank=True)
    def __str__(self):
        return f'{self.title}'


class Post (models.Model):
    # auther = user
    poster = models.ImageField(upload_to='post_posters/', null=True , blank=True )
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)