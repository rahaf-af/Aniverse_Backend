from django.urls import path
from .views import Signup, AnimeIndex , AnimeDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh' ),
    path('animes/',AnimeIndex.as_view() , name= 'Anime_Index'),
    path('anime/<int:Anime_id>/', AnimeDetail.as_view(), name= 'Anime_Detail')
] 