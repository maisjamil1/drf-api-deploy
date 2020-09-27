from django.urls import path

from .views import MoviesList, MovieDetails

urlpatterns = [
    path('', MoviesList.as_view(), name='movies'),
    path('<int:pk>/', MovieDetails.as_view(), name='movie_details') 
]