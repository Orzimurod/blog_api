from django.shortcuts import render
from rest_framework import viewsets

from api.models import Category,Post
from api.serializers import CategorySerializer, PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


