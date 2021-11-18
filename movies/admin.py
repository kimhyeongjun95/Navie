from django.contrib import admin
from .models import Movie, Genre, Actor, Director, Keyword

# Register your models here.
admin.site.register([Movie, Genre, Actor, Director, Keyword])