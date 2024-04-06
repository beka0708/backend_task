from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.UserListCreateAPIView.as_view(), name="user_list"),
    path("profile/", views.ProfileListCreateAPIView.as_view(), name="profile_list"),
    path("profile/<int:pk>", views.ProfileDetailAPIView.as_view(), name="post_list_id"),
    path("review/", views.ReviewListCreateAPIView.as_view(), name="review_list"),
    path("hashtag/", views.HashTagListCreateAPIView.as_view(), name="hashtag_list"),
    path(
        "hashtag/<int:pk>", views.HashTagDetailAPIView.as_view(), name="hashtag_list_id"
    ),
    path("post/", views.PostListCreateAPIView.as_view(), name="post_list_create"),
    path("post/<int:pk>/", views.PostDetailAPIView.as_view(), name="post_detail"),
]
