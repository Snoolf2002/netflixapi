from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from movie.models import Movie, Actor, Comment
from movie.serializers import ActorSerializer, CommentSerializer, MovieSerializer


class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
        

class ActorAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)


class MovieViewSet(ModelViewSet):
    queryset            = Movie.objects.all()
    serializer_class    = MovieSerializer
    filter_backends     = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields       = ['title', 'actors__name']
    ordering_fields     = ['imdb', '-imdb']
    filterset_fields    = ['genre']
    

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    
class CommentAPIView(APIView):
    def get(self, request):
        todos = Comment.objects.filter(user_id=self.request.user.id)
        serializer = CommentSerializer(todos, many=True)
        
        return Response(data=serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 
    
    def get_queryset(self):
        return Comment.objects.filter(user_id = self.request.user)
    
    def perform_create(self, serializer):
        serializer.validated_data["user_id"] = self.request.user
        serializer.save()
        