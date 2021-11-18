from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


# Create your models here.
class User(AbstractUser):
    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    like_movies = models.ManyToManyField(Movie, related_name='like_users')
    recommend_movies = models.ManyToManyField(Movie, related_name='recommend_users')

    def __str__(self):
        return self.user_id