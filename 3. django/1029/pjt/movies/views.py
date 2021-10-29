from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Actor, Movie, Review
from .serializers import ActorsListSerializer, ActorSerializer, MoviesListSerializer, MovieSerializer, ReviewsListSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def actors_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorsListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MoviesListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        starring = request.data.pop('starring')
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie = serializer.save()
            for star in starring:
                movie.actors.add(star)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def reviews_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewsListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            '삭제 요청이 처리되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)