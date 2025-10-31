from .models import User,Anime, Profile, Post , Review, AnimeFavorit, PostComment, PostFavorit
from rest_framework import serializers


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name" , "last_name", "password" ]
        extra_kwargs ={
            "password": {"write_only": True}
        }

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