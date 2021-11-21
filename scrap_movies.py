import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from movies.models import Movie, Genre, Actor, Director, Keyword
import requests
from django.shortcuts import get_object_or_404


def scrap_genre_list():
    genre_list_res = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=3a5be8d94b0edc5a4cd336281a27127e&language=ko-KR').json()
    
    for genre in genre_list_res['genres']:
        Genre.objects.create(id_code=genre['id'], name=genre['name'])


def scrap_credit_list(movie_id):
    #movie/무비 id
    credit_list_res = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=3a5be8d94b0edc5a4cd336281a27127e&language=ko-KR').json()
    return credit_list_res


def scrap_keyword_list(movie_id):
    #movie/무비 id
    keyword_list_res = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key=3a5be8d94b0edc5a4cd336281a27127e').json()
    return keyword_list_res


def scrap_movie_list():
    #list/리스트 id
    for i in range(20, 1000):
        movie_list_res = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key=3a5be8d94b0edc5a4cd336281a27127e&language=ko-KR&page={i}').json()
        try:
            movie_list_res['results']
            for m in movie_list_res['results']:
                if m and Movie.objects.filter(id_code=m['id']).exists():
                    continue
                else:
                    movie = Movie()
                    try:
                        movie.id_code = m['id']
                    except:
                        continue
                    try:
                        movie.title = m['title']
                    except:
                        continue
                    try:
                        movie.plot = m['overview']
                    except:
                        continue
                    try:
                        movie.release_date = m['release_date']
                    except:
                        continue
                    try:
                        movie.poster_path = m['poster_path']
                    except:
                        continue
                    try:
                        movie.backdrop_path = m['backdrop_path']
                    except:
                        pass
                    movie.save()

                    for g_id in m['genre_ids']:
                        genre = get_object_or_404(Genre, id_code=g_id)
                        movie.genres.add(genre)
                    
                    credit_list = scrap_credit_list(movie.id_code)
                    if credit_list['cast']:
                        for credit in credit_list['cast']:
                            if credit['known_for_department'] == 'Acting':
                                if Actor.objects.filter(id_code=credit['id']).exists():
                                    actor = get_object_or_404(Actor, id_code=credit['id'])
                                    movie.actors.add(actor)
                                else:
                                    Actor.objects.create(id_code=credit['id'], name=credit['name'])
                                    actor = get_object_or_404(Actor, id_code=credit['id'])
                                    movie.actors.add(actor)
                            elif credit['known_for_department'] == 'Directing':
                                if Director.objects.filter(id_code=credit['id']).exists():
                                    director = get_object_or_404(Director, id_code=credit['id'])
                                    movie.directors.add(director)
                                else:
                                    Director.objects.create(id_code=credit['id'], name=credit['name'])
                                    director = get_object_or_404(Director, id_code=credit['id'])
                                    movie.directors.add(director)
                    
                    keyword_list = scrap_keyword_list(movie.id_code)
                    if keyword_list['keywords']:
                        for keyword in keyword_list['keywords']:
                            if Keyword.objects.filter(id_code=keyword['id']).exists():
                                word = get_object_or_404(Keyword, id_code=keyword['id'])
                                movie.keywords.add(word)
                            else:
                                Keyword.objects.create(id_code=keyword['id'], name=keyword['name'])
                                word = get_object_or_404(Keyword, id_code=keyword['id'])
                                movie.keywords.add(word)
        except:
            pass

        

# scrap_genre_list()
scrap_movie_list()