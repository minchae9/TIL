from .models import Actor, Movie, Review
from rest_framework import serializers

class ActorsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id','name',)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        depth = 1


class MoviesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)
        depth = 1


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorsListSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    starring = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewsListSerializer(serializers.ModelSerializer):
    movie = MoviesListSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('movie', 'title',)