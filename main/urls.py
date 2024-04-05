from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserListCreateAPIView.as_view(), name='post_list_create'),
    path('profile/', views.ProfileListCreateAPIView.as_view(), name='post_list_create'),
    path('profile/<int:pk>', views.ProfileDetailAPIView.as_view(), name='post_list_create'),
    path('review/', views.ReviewListCreateAPIView.as_view(), name='post_list_create'),
    path('hashtag/', views.HashTagListCreateAPIView.as_view(), name='post_list_create'),
    path('hashtag/<int:pk>', views.HashTagDetailAPIView.as_view(), name='post_list_create'),
    path('post/', views.PostListCreateAPIView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', views.PostDetailAPIView.as_view(), name='post_detail'),
]
