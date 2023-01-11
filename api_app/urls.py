from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api_app import views

app_name = 'api_app'

schema_view = get_schema_view(
   openapi.Info(
      title="Virtual Movie API",
      default_version='v1',
      description="AN Open API that allows consumption of it data",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('all_movies/', views.MoviesListView.as_view()),
    path('add_movie/',views.MovieCreateView.as_view()),
    path('movies/search/', views.search),
    path('movies/<slug:category_slug>/<slug:movie_slug>/', views.MovieDetailView.as_view()),
    path('add_category/',views.CategoryCreateView.as_view()),
    path('movies/<slug:category_slug>/', views.CategoryDetailView.as_view()),
    path('add_media/',views.MediaCreateView.as_view()),
    path('media/<slug:media_slug>/', views.MediaDetailView.as_view()),
    path('add_country/',views.CountryCreateView.as_view()),
    path('country/<slug:country_slug>/', views.CountryDetailView.as_view()),
    path('add_language/',views.LanguageCreateView.as_view()),
    path('language/<slug:language_slug>/', views.LanguageDetailView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)