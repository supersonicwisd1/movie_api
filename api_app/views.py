from django.shortcuts import render

from django.db.models import Q
from django.shortcuts import Http404, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import CreateAPIView,ListCreateAPIView
# from rest_framework.pagination import PageNumberPagination


from .serializers import MovieSerializer, CategorySerializer, MediaSerializer, LanguageSerializer, CountrySerializer
from .models import Movie, Category, Media, Country, Language


class MoviesListView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()[0:4]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieCreateView(CreateAPIView):
    serializer_class=MovieSerializer
    
class MovieDetailView(APIView):
    def get_object(self, category_slug, movie_slug):
        try:
            return Movie.objects.filter(category__slug=category_slug).get(slug=movie_slug)
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, movie_slug, format=None):
        movie = self.get_object(category_slug, movie_slug)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class CategoryDetailView(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
class CategoryCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MediaDetailView(APIView):
    def get_object(self, media_slug):
        try:
            return Media.objects.get(slug=media_slug)
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, media_slug, format=None):
        media = self.get_object(media_slug)
        serializer = MediaSerializer(media)
        return Response(serializer.data)
    
class MediaCreateView(ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    
class CountryDetailView(APIView):
    def get_object(self, country_slug):
        try:
            return Country.objects.get(slug=country_slug)
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, country_slug, format=None):
        country = self.get_object(country_slug)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

class CountryCreateView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
class LanguageDetailView(APIView):
    def get_object(self, language_slug):
        try:
            return Language.objects.get(slug=language_slug)
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, language_slug, format=None):
        language = self.get_object(language_slug)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

class LanguageCreateView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    
    if query:
        movies = Movie.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        return Response({"movies": []})