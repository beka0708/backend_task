from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from . import forms
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .models import Post, User, Review, Profile, HashTag
from .serializers import (
    PostSerializer,
    UserSerializer,
    ReviewSerializer,
    ProfileSerializer,
    HashTagSerializer,
)
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class CreatePostView(CreateView):
    template_name = 'create_post.html'
    form_class = forms.PostForm
    success_url = "/post_list/"

    def form_valid(self, form):
        new_post = form.save()
        users = User.objects.all()
        channel_layer = get_channel_layer()
        for user in users:
            async_to_sync(channel_layer.group_send)(
                f'user_{user.id}',
                {
                    'type': 'notify_new_post',
                    'new_post': PostSerializer(new_post).data,
                }
            )
        return super().form_valid(form)


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})


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


def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostDetailView(DetailView):
    template_name = "post_detail.html"

    def get_object(self, **kwargs):
        post_id = self.kwargs.get("id")
        return get_object_or_404(Post, id=post_id)


class PostUpdateView(UpdateView):
    template_name = "update_post.html"
    form_class = forms.PostForm
    success_url = "/posts/"

    def get_object(self, **kwargs):
        post_id = self.kwargs.get("id")
        return get_object_or_404(Post, id=post_id)

    def form_valid(self, form):
        return super(PostUpdateView, self).form_valid(form=form)


class PostDeleteView(DeleteView):
    template_name = "delete_post.html"
    success_url = "/posts/"

    def get_object(self, **kwargs):
        post_id = self.kwargs.get("id")
        return get_object_or_404(Post, id=post_id)


class HashTagListCreateAPIView(generics.ListCreateAPIView):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer


class HashTagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer
