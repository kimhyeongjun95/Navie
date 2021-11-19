from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    like_movies = models.ManyToManyField(Movie, related_name='like_users')
    recommend_movies = models.ManyToManyField(Movie, related_name='recommend_users')

    def __str__(self):
        return self.username