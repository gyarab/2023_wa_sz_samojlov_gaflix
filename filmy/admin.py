from django.contrib import admin
from filmy.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)

