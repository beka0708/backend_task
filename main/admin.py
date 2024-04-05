from django.contrib import admin
from .models import User, Profile, HashTag, Post, Review

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(HashTag)
admin.site.register(Post)
admin.site.register(Review)
