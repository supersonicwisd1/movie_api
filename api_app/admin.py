from django.contrib import admin

from api_app.models import Category, Movie, Media, Country, Language

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Media)
admin.site.register(Country)
admin.site.register(Language)