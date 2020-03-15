from django.shortcuts import render
from rest_framework import generics, permissions
from blog.models import Article
from .serializers import PostSerializer

# Create your views here.

class PostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostSerializer

class PostAPIDetailView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostSerializer