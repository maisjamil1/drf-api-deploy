- `mkdir drf-api`
- `cd drf-api`
- `poetry init -n`
- `poetry add django djangorestframework`
- `poetry shell`
- `django-admin startproject movies_project .`
- `python manage.py  migrate`
- `python manage.py  startapp movie`
- `python manage.py  createsuperuser`
- `python manage.py  runserver`
______________________________________________
- in the `settings.py` ---> INSTALLED_APPS --->add the app to project applications `'movie.apps.MovieConfig',`
- go to `movie/models.py` ----> 
```python
from django.contrib.auth import get_user_model
from django.db import models

class Movies(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

```
- `python manage.py makemigrations movie`
- `python manage.py migrate`

- go to  movie/`admin.py` ----> add :
```python
from django.contrib import admin

from .models import Movies
# Register your models here.

admin.site.register(Movies)

```
- `python manage.py runserver`
- do tests
- in the `settings.py` ---> INSTALLED_APPS --->add the app to project applications `'rest_framework',`
- in the `settings.py` add:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASS': [
        'rest_framework.permissions.AllowAny',
    ]
}
```
- in movies_project/`urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', include('movie.urls')),
]

```

- create movie/`serializer.py` to convert data to json:
```python
from rest_framework import serializers

from .models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'body', 'created_at')
        model = Movies

```
- in movie/`views.py`:
```python 
from django.shortcuts import render
from rest_framework import generics

from .models import Movies
from .serializer import MoviesSerializer

class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
```
- in movie/`urls.py`:
```python
from django.urls import path

from .views import MoviesList, MovieDetails

urlpatterns = [
    path('', MoviesList.as_view(), name='movies'),
    path('<int:pk>/', MovieDetails.as_view(), name='movie_details') 
]

```
- `python manage.py  runserver`
