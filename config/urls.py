from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main.views import (
    user_list,
    post_list,
    PostDetailView,
    CreatePostView,
    PostUpdateView,
    PostDeleteView,
)
from .swagger import urlpatterns as swagger_yasg

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api/v1/", include("main.urls")),
        path("users/", user_list, name="user-list-html"),
        path("posts/", post_list, name="post-list-html"),
        path("create_post/", CreatePostView.as_view(), name="create_post"),
        path("posts/<int:id>/", PostDetailView.as_view(), name="post-detail-html"),
        path(
            "posts/<int:id>/update", PostUpdateView.as_view(), name="post-update-html"
        ),
        path(
            "posts/<int:id>/delete", PostDeleteView.as_view(), name="post-delete-html"
        ),

    ]
    + swagger_yasg
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

)
