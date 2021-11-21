from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe, require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Genre, Movie, Actor, Director, Keyword
from reviews.models import Review
import requests
from django.http import JsonResponse
import random


# Create your views here.
@require_safe
def index(request):
    recent_movies = Movie.objects.all().order_by('-release_date')[:15]
    action_movies = Movie.objects.filter(genres=1).order_by('-release_date')[:15]
    romance_movies = Movie.objects.filter(genres=14).order_by('-release_date')[:15]
    crime_movies = Movie.objects.filter(genres=80).order_by('-release_date')[:15]
    horror_movies = Movie.objects.filter(genres=27).order_by('-release_date')[:15]
    comedy_movies = Movie.objects.filter(genres=35).order_by('-release_date')[:15]
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


@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            liked = False
        else:
            movie.like_users.add(request.user)
            liked = True

        context = {
            'liked': liked,
        }
        return JsonResponse(context)


@login_required
@require_safe
def recommend_movies(request):
    return render(request, 'movies/recommend_movies.html')


def movies_worldcup(request):
    action = Movie.objects.filter(genres=1)
    romance = Movie.objects.filter(genres=14)
    crime = Movie.objects.filter(genres=5)
    horror = Movie.objects.filter(genres=11)
    comedy = Movie.objects.filter(genres=4)
    sf = Movie.objects.filter(genres=15)
    family = Movie.objects.filter(genres=8)
    music = Movie.objects.filter(genres=12)
    
    # 8개 장르 영화 중복없이 넣기
    random_movies = []
    print(random_movies)
    # 액션 영화
    action_movie = random.choice(action)
    random_movies.append([action_movie.pk, action_movie.poster_path, action_movie.title])

    # 로맨스 영화
    while True:
        romance_movie = random.choice(romance)
        if romance_movie.pk != action_movie.pk:
            random_movies.append([romance_movie.pk, romance_movie.poster_path, romance_movie.title])
            break
    
    # 범죄 영화
    while True:
        crime_movie = random.choice(crime)
        if action_movie.pk != crime_movie.pk and romance_movie.pk != crime_movie.pk:
            random_movies.append([crime_movie.pk, crime_movie.poster_path, crime_movie.title])
            break
    
    # 공포 영화
    while True:
        horror_movie = random.choice(horror)
        if action_movie.pk != horror_movie.pk and romance_movie.pk != horror_movie.pk and crime_movie.pk != horror_movie.pk:
            random_movies.append([horror_movie.pk, horror_movie.poster_path, horror_movie.title])
            break
    
    # 코미디 영화
    while True:
        comedy_movie = random.choice(comedy)
        if action_movie.pk != comedy_movie.pk and romance_movie.pk != comedy_movie.pk and crime_movie.pk != comedy_movie.pk and horror_movie.pk != comedy_movie.pk:
            random_movies.append([comedy_movie.pk, comedy_movie.poster_path, comedy_movie.title])
            break
    
    # sf 영화
    while True:
        sf_movie = random.choice(sf)
        if action_movie.pk != sf_movie.pk and romance_movie.pk != sf_movie.pk and crime_movie.pk != sf_movie.pk and horror_movie.pk != sf_movie.pk and comedy_movie.pk != sf_movie:
            random_movies.append([sf_movie.pk, sf_movie.poster_path, sf_movie.title])
            break
    
    # 가족 영화
    while True:
        family_movie = random.choice(family)
        if action_movie.pk != family_movie.pk and romance_movie.pk != family_movie.pk and crime_movie.pk != family_movie.pk and horror_movie.pk != family_movie.pk and comedy_movie.pk != family_movie.pk and sf_movie.pk != family_movie.pk:
            random_movies.append([family_movie.pk, family_movie.poster_path, family_movie.title])
            break
    
    # 음악 영화
    while True:
        music_movie = random.choice(music)
        if action_movie.pk != music_movie.pk and romance_movie.pk != music_movie.pk and crime_movie.pk != music_movie.pk and horror_movie.pk != music_movie.pk and comedy_movie.pk != music_movie.pk and sf_movie.pk != music_movie.pk and family_movie.pk != music_movie.pk:
            random_movies.append([music_movie.pk, music_movie.poster_path, music_movie.title])
            break
    
    context = {
        'random_movies': random_movies,
    }
    print(context)
    return JsonResponse(context, safe=False)


@login_required
@require_safe
def result_recommend(request, movie1_pk, movie2_pk):
    movie1 = get_object_or_404(Movie, pk=movie1_pk)
    movie2 = get_object_or_404(Movie, pk=movie2_pk)

    genres1 = movie1.genres.all()
    genres2 = movie2.genres.all()

    for g1 in genres1:
        for g2 in genres2:
            if g1.pk != g2.pk:
                genre1 = g1
                genre2 = g2
    
    genre1_movie1 = random.choice(genre1.movies.all())
    while True:
        genre1_movie2 = random.choice(genre1.movies.all())
        if genre1_movie1.pk != genre1_movie2.pk:
            break
    
    genre2_movie3 = random.choice(genre2.movies.all())
    while True:
        genre2_movie4 = random.choice(genre2.movies.all())
        if genre2_movie3.pk != genre2_movie4.pk:
            break

    request.user.recommend_movies.add(genre1_movie1)
    request.user.recommend_movies.add(genre1_movie2)
    request.user.recommend_movies.add(genre2_movie3)
    request.user.recommend_movies.add(genre2_movie4)
    context = {
        'movie1': movie1,
        'movie2': movie2,
        'genre1_movie1': genre1_movie1,
        'genre1_movie2': genre1_movie2,
        'genre2_movie3': genre2_movie3,
        'genre2_movie4': genre2_movie4,
    }
    return render(request, 'movies/result_recommend.html', context)