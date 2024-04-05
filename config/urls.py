from django.contrib import admin
from django.urls import path, include

from .swagger import urlpatterns as swagger_yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
] + swagger_yasg


