from django.contrib import admin
from .models import  User,Anime, Profile, Post , Review, AnimeFavorit, PostComment, PostFavorit

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Anime)
admin.site.register(AnimeFavorit)
admin.site.register(Review)
admin.site.register(Post)
admin.site.register(PostFavorit)
admin.site.register(PostComment)

