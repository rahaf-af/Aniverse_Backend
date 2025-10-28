from django.urls import path
from .views import AnimeIndex , AnimeDetail

urlpatterns = [
    path('animes/',AnimeIndex.as_view() , name= 'Anime_Index'),
    path('anime/<int:Anime_id>/', AnimeDetail.as_view(), name= 'Anime_Detail')
]