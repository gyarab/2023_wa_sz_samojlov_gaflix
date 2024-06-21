from django.shortcuts import render

from .models import Movie, Director, Actor, Genre
from django.db.models import Q


def movies(request):
    movies_queryset = Movie.objects.all()

    ## ziskani zanru z DB
    genre = request.GET.get("genre")

    if genre:
        movies_queryset = movies_queryset.filter(genres__name=genre)

    search = request.GET.get("search")
    
    if search:
        movies_queryset = movies_queryset.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )

    context = {
        "movies": movies_queryset,
        "genres": Genre.objects.all().order_by("name"),
        "genre": genre,
        "search": search,
    }
    return render(request, "filmy/movies.html", context)


def movie(request, id):
    m = Movie.objects.get(id=id)

    context = {
        "movie": m,
    }
    return render(request, "filmy/movie.html", context)


def directors(request):

    directors_queryset = Director.objects.all()

    context = {
        "directors": directors_queryset
    }
    return render(request, "filmy/directors.html", context)


def director(request, id):

    m = Director.objects.get(id=id)

    context = {
        "director": m,
    }
    return render(request, "filmy/director.html", context)

def actors(request):

    actors_queryset = Actor.objects.all()

    context = {
        "actors": actors_queryset
    }
    return render(request, "filmy/actors.html", context)


def actor(request, id):
    
    m = Actor.objects.get(id=id)

    context = {
        "actor": m,
    }
    return render(request, "filmy/actor.html", context)