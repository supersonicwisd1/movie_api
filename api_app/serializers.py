from rest_framework import serializers

from api_app.models import Category, Movie, Media, Language, Country

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "adult",
            "id",
            "name",
            "original_name",
            'original_language',
            'original_country',
            "get_language",
            "get_country",
            "get_absolute_url",
            "overview",
            'media_type',
            "get_category",
            "rating",
            "popularity",
            "vote_count",
            "vote_average",
            'poster_path',
            'poster_thumbnail_path',
            'triller_path',
            'movie_path',
            "get_image",
            "get_thumbnail",
            "date_released",
            "get_triller",
            "get_movie",
        )

class CategorySerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "movies",
        )
        
class MediaSerializer(serializers.ModelSerializer):
    mediatypes = MovieSerializer(many=True)
    
    class Meta:
        model = Media
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "mediatypes",
        )
        
class CountrySerializer(serializers.ModelSerializer):
    countries = MovieSerializer(many=True)
    
    class Meta:
        model = Country
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "countries",
        )
                
class LanguageSerializer(serializers.ModelSerializer):
    languages = MovieSerializer(many=True)
    
    class Meta:
        model = Language
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "languages",
        )