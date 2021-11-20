from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from django.db.models import Q
from .models import Genre, Movie, Actor, Director, Keyword
from reviews.models import Review
import requests


# Create your views here.
@require_safe
def index(request):
    recent_movies = Movie.objects.all().order_by('-release_date')
    action_movies = Movie.objects.filter(genres=1).order_by('-release_date')
    romance_movies = Movie.objects.filter(genres=14).order_by('-release_date')
    crime_movies = Movie.objects.filter(genres=80).order_by('-release_date')
    horror_movies = Movie.objects.filter(genres=27).order_by('-release_date')
    comedy_movies = Movie.objects.filter(genres=35).order_by('-release_date')
    context = {
        'recent_movies': recent_movies,
        'action_movies': action_movies,
        'romance_movies': romance_movies,
        'crime_movies': crime_movies,
        'horror_movies': horror_movies,
        'comedy_movies': comedy_movies,

    }
    return render(request, 'movies/index.html', context)


@require_safe
def search(request):
    word = request.GET.get('word')
    print(word, '결과')
    movies = Movie.objects.filter(Q(title__icontains=word) | Q(plot__icontains=word))
    reviews = Review.objects.filter(Q(title__icontains=word) | Q(content__icontains=word))
    genres = Genre.objects.filter(Q(name__icontains=word))
    actors = Actor.objects.filter(name__icontains=word)
    directors = Director.objects.filter(name__icontains=word)
    keywords = Keyword.objects.filter(name__icontains=word)

    context = {
        'movies': movies,
        'reviews': reviews,
        'genres': genres,
        'actors': actors,
        'directors': directors,
        'keywords': keywords,
    }
    return render(request, 'movies/search.html', context)


@require_safe
def detail_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    get_movie_video = requests.get(f'https://api.themoviedb.org/3/movie/{movie.id_code}/videos?api_key=3a5be8d94b0edc5a4cd336281a27127e&language=ko-KR').json()
    youtube_key = False
    try:
        for video in get_movie_video['results']:
            if video['type'] == 'Official Teaser':
                youtube_key = video['key']
                break
        else:
            for video in get_movie_video['results']:
                if video['type'] == 'Teaser':
                    youtube_key = video['key']
                    break
            else:
                for video in get_movie_video['results']:
                    if video['type'] == 'Trailer':
                        youtube_key = video['key']
                        break
    except:
        pass
    
    context = {
        'movie': movie,
        'youtube_key': youtube_key,
    }
    return render(request, 'movies/detail_movie.html', context)
    # <iframe
    #   width="560"
    #   height="315"
    #   src="https://www.youtube.com/embed/{{ youtube_key }}"
    #   title="YouTube video player"
    #   frameborder="0"
    #   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    #   allowfullscreen
    #  >
    # </iframe>