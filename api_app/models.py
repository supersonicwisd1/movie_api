from io import BytesIO
from PIL import Image

from django.core.validators import FileExtensionValidator
from django.core.files import File
# from djangocountries.fields import CountryFieldv 
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/(self.slug)/'
    
class Media(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/(self.slug)/'
    
class Country(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/(self.slug)/'
    
class Language(models.Model):
    name = models.CharField(max_length=3)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/(self.slug)/'
        
    
class Movie(models.Model):
    category = models.ForeignKey(Category, related_name='movies', on_delete=models.CASCADE)
    adult = models.CharField(max_length=5, choices=(
        ('true','true'),
        ('false', 'false')     
    ))
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    original_name = models.CharField(max_length=300)
    
    original_language = models.ForeignKey(Language, related_name="languages", on_delete=models.CASCADE)
     
    original_country = models.ForeignKey(Country, related_name="countries", on_delete=models.CASCADE)
    media_type = models.ForeignKey(Media, related_name="mediatypes", on_delete=models.CASCADE) 
    overview = models.TextField()
    
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    popularity = models.DecimalField(max_digits=8, decimal_places=3)
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=3)
    
    poster_path = models.ImageField(upload_to='uploads/', null=False,blank=False)
    poster_thumbnail_path = models.ImageField(upload_to='uploads/', null=False,blank=False)
    triller_path = models.FileField(upload_to='vidoes_uploaded', null=False,
                               validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    movie_path = models.FileField(upload_to='vidoes_uploaded', null=True,
                               validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    
    date_released = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_category(self):
        return self.category.name
    
    def get_language(self):
        return self.original_language.name
    
    def get_country(self):
        return self.original_country.name
    
    def get_image(self):
        if self.poster_path:
            return "http://127.0.0.1:8000" + self.poster_path.url
        return ""
    
    def get_thumbnail(self):
        if self.poster_thumbnail_path:
            return "http://127.0.0.1:8000" + self.poster_thumbnail_path.url
        else:
            if self.image:
                self.poster_thumbnail_path = self.make_thumbnail(self.image)
                self.save()
                
                return self.poster_thumbnail_path.url
            else:
                return "http//via.placeholder.com/240x180.jpg"
            
    def make_thumbnail(self, poster_path, size=(250, 250)):
        img = Image.open(poster_path)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        
        thumbnail  = File(thumb_io, name=poster_path.name)
        
        return thumbnail
    
    def get_triller(self):
            if self.triller_path:
                return "http://127.0.0.1:8000" + self.triller_path.url
            return ""
        
    def get_movie(self):
            if self.movie_path:
                return "http://127.0.0.1:8000" + self.movie_path.url
            return ""