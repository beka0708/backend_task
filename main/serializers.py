from rest_framework import serializers
from .models import User, Profile, HashTag, Post, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    hashtag = HashTagSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Post
        fields = 'id user title image description hashtag created_date'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
