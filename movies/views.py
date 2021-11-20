from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Genre, Movie, Actor, Director, Keyword
from reviews.models import Review
import requests


# Create your views here.
def index(request):
    return render(request, 'base.html')


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