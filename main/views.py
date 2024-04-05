from rest_framework import generics

from .models import Post, User, Review, Profile, HashTag
from .serializers import (
    PostSerializer,
    UserSerializer,
    ReviewSerializer,
    ProfileSerializer,
    HashTagSerializer,
)


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class HashTagListCreateAPIView(generics.ListCreateAPIView):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer


class HashTagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer
