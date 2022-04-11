from rest_framework import serializers
from movie.models import Movie, Actor, Comment




class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'birthdate', 'gender']


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'imdb', 'genre', 'actors']
    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    