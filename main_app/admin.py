from django.contrib import admin
from .models import Anime, User , Post, Profile

# Register your models here.
admin.site.register(Anime)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Profile)
