from django.urls import path
from .views import Signup,DeleteUser,ProfileDetail, AnimeIndex , AnimeDetail , PostIndex , PostDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('deleteuser/', DeleteUser.as_view(), name='delete_user'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh' ),
    path('Profile/<int:Profile_id>/', ProfileDetail.as_view(), name= 'Profile_Detail'),
    path('animes/',AnimeIndex.as_view() , name= 'Anime_Index'),
    path('anime/<int:Anime_id>/', AnimeDetail.as_view(), name= 'Anime_Detail'),
    path('posts/',PostIndex.as_view() , name= 'Post_Index'),
    path('post/<int:Post_id>/', PostDetail.as_view(), name= 'Post_Detail')
] 