from django.urls import path
from .views import Signup, DeleteUser, ProfileDetail, AnimeIndex, AnimeDetail, AddAnimeToFavorit, AnimeReviewIndex, DeleteAnimeReview, PostIndex, PostDetail, PostCommentIndex, DeletePostComment
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('deleteuser/', DeleteUser.as_view(), name='delete_user'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh' ),
    path('profile/<int:profile_id>/', ProfileDetail.as_view(), name= 'Profile_Detail'),
    path('animes/',AnimeIndex.as_view() , name= 'Anime_Index'),
    path('anime/<int:Anime_id>/', AnimeDetail.as_view(), name= 'Anime_Detail'),
    path('add/<int:Anime_id>/tofavorit', AddAnimeToFavorit.as_view(), name= 'Add_Anime_To_Favorit'),
    path('anime/<int:Anime_id>/review', AnimeReviewIndex.as_view(), name= 'Anime_Review_Index'),
    path('delete/<int:Review_id>/review', DeleteAnimeReview.as_view(), name= 'Anime_Review_Index'),
    path('posts/',PostIndex.as_view() , name= 'Post_Index'),
    path('post/<int:Post_id>/', PostDetail.as_view(), name= 'Post_Detail'),
    path('post/<int:Post_id>/comment', PostCommentIndex.as_view(), name= 'Anime_Review_Index'),
    path('delete/<int:Comment_id>/comment', DeletePostComment.as_view(), name= 'Anime_Review_Index'),

] 