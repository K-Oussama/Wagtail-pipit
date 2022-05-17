from rest_framework import generics
from django.shortcuts import render
from main.views import post


from main.models import Category
from main.serializers import CategorySerializer, PostSerializer




class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all() #.filter(level=1)
    serializer_class = CategorySerializer

class CategoryItemView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return post.Post.objects.filter(
            category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )