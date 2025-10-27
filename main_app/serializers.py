from .models import Anime
from rest_framework import serializers

class Animeserializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'