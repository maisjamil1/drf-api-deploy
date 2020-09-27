from django.shortcuts import render
from rest_framework import generics

from .models import Movies
from .serializer import MoviesSerializer

class MoviesList(generics.ListCreateAPIView):
    #ListCreateAPIView it allows u to add from restapi page
    #ListAPIView -->go to admin page to add things
    queryset = Movies.objects.all()#give me all movies
    serializer_class = MoviesSerializer# convert movies to json

class MovieDetails(generics.RetrieveUpdateDestroyAPIView):#to update and delete
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer