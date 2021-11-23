from django.db import models


# Create your models here.
class Genre(models.Model):
    id_code = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    id_code = models.IntegerField()
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Director(models.Model):
    id_code = models.IntegerField()
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    id_code = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.word


class Movie(models.Model):
    id_code = models.IntegerField()
    title = models.CharField(max_length=100)
    plot = models.TextField(null=True)
    release_date = models.CharField(max_length=50, null=True)
    poster_path = models.TextField(null=True)
    backdrop_path = models.TextField(null=True)
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')
    keywords = models.ManyToManyField(Keyword, related_name='movies')

    def __str__(self):
        return self.title









