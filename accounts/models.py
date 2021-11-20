from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='profile-images')
    image_thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFill(40, 40)])
    like_movies = models.ManyToManyField(Movie, related_name='like_users')
    recommend_movies = models.ManyToManyField(Movie, related_name='recommend_users')

    def __str__(self):
        return self.username