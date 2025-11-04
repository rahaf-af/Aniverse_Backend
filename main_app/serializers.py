from .models import User,Anime, Profile, Post , Review, AnimeFavorit, PostComment, PostFavorit ,Contact
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
    first_name  = serializers.CharField(source= 'user.first_name', read_only = True)
    last_name  = serializers.CharField(source= 'user.last_name', read_only = True)
    username = serializers.CharField(source= 'user.username', read_only = True)
    email = serializers.CharField(source= 'user.email', read_only = True)
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Profile
        fields = '__all__'

class Animeserializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()
    review_count = serializers.IntegerField(source= 'anime_comment.count', read_only = True)
    favorit_count = serializers.IntegerField(source= 'anime_favorit.count', read_only = True)
    class Meta:
        model = Anime
        fields = '__all__'

class AnimeFavoritserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    anime = serializers.StringRelatedField()
    anime_id = serializers.IntegerField(source= 'anime.id', read_only = True)
    anime_poster = serializers.CharField(source= 'anime.poster', read_only = True)
    class Meta:
        model = AnimeFavorit
        fields = '__all__'

class Reviewserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    anime = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ['id','user','anime', 'text', 'rating', 'created_at' ]

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class Postserializer(serializers.ModelSerializer):
    auther = serializers.StringRelatedField()
    comment_count = serializers.IntegerField(source= 'post_comment.count', read_only = True)
    favorit_count = serializers.IntegerField(source= 'post_favorit.count', read_only = True)
    class Meta:
        model = Post
        fields = '__all__'

class PostFavoritserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    post_poster = serializers.CharField(source= 'post.poster', read_only = True)
    user_username = serializers.CharField(source= 'user.username', read_only = True)
    class Meta:
        model = PostFavorit
        fields = '__all__'

class PostCommentserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    class Meta:
        model = PostComment
        fields = ['id','user','post', 'text', 'created_at' ]

class Contacteserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Contact
        fields = '__all__'