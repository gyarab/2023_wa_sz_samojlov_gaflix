from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor

# Register your models here.
class MovieAdmin(admin.ModelAdmin):

    ## zobrazeni listu v tabulce Movie
    list_display = ['id', 'name', 'year', 'footage', 'genres_display', 'director']

    ## odkazy v seznamu, vyber polozek ktere budou klikaci
    list_display_links = ['id', 'name']

    ## moznost hledani v seznamu
    search_fields = ['name', 'director_name']

    ## filtr seznamu
    list_filter = ['genres', 'year']
    pass

class DirectorAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

class ActorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)

admin.site.register(Actor, ActorAdmin)
