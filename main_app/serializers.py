from .models import User,Anime, Profile, Post , Review, AnimeFavorit, PostComment, PostFavorit
from rest_framework import serializers


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name" , "last_name","email", "password" ]
        extra_kwargs ={
            "password": {"write_only": True}
        }
    def create (self , validated_data):
            user = User.objects.create_user(
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                username = validated_data['username'],
                email = validated_data['email'],
                password = validated_data['password']
            )
            user.save()
            return user

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class Animeserializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField(source= 'anime_comment.count', read_only = True)
    favorit_count = serializers.IntegerField(source= 'anime_favorit.count', read_only = True)
    class Meta:
        model = Anime
        fields = '__all__'

class Reviewserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ['id','user','anime', 'text', 'rating', 'created_at' ]

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class Postserializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source= 'post_comment.count', read_only = True)
    favorit_count = serializers.IntegerField(source= 'post_favorit.count', read_only = True)
    class Meta:
        model = Post
        fields = '__all__'

class PostCommentserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = PostComment
        fields = ['id','user','post ', 'text', 'created_at' ]
