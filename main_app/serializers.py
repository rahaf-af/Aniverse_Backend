from .models import Anime, Profile, Post , Review, AnimeFavorit, PostComment, PostFavorit
from rest_framework import serializers

class Animeserializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'