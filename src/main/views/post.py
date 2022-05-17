from rest_framework import generics
from django.shortcuts import render


from main.models import Category, Post
from main.serializers import CategorySerializer, PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class Post(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostSerializer