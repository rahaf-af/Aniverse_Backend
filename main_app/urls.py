from django.urls import path
from .views import Signup, Handeluser,MyProfile, ProfileDetail, AnimeIndex, AnimeDetail, AddAnimeToFavorit, RemoveAnimeFromFavorit, AnimeReviewIndex, MyAnimeToFavoritList, DeleteAnimeReview, PostIndex, PostDetail, AddPostToFavorit, RemovePostFromFavorit, MyPostToFavoritList, PostCommentIndex, DeletePostComment, Contactus, Homeanime,Homeposts
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('handeluser/', Handeluser.as_view(), name='handel_user'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh' ),
    path('contact/',Contactus.as_view(), name='contact_us' ),
    path('homeanime/',Homeanime.as_view(), name='homeanime' ),
    path('homeposts/',Homeposts.as_view(), name='homeposts' ),
    path('profile/<int:Profile_id>/', ProfileDetail.as_view(), name= 'Profile_Detail'),
    path('myprofile/', MyProfile.as_view(), name= 'MyProfile'),
    path('animes/',AnimeIndex.as_view() , name= 'Anime_Index'),
    path('anime/<int:Anime_id>/', AnimeDetail.as_view(), name= 'Anime_Detail'),
    path('addanime/<int:Anime_id>/tofavorit/', AddAnimeToFavorit.as_view(), name= 'Add_Anime_To_Favorit'),
    path('removeanime/<int:Favorit_id>/fromfavorit/', RemoveAnimeFromFavorit.as_view(), name= 'Remove_Anime_From_Favorit'),
    path('myanimefavoritlist/',MyAnimeToFavoritList.as_view() , name= 'My_Anime_Favorit_List'),
    path('anime/<int:Anime_id>/review/', AnimeReviewIndex.as_view(), name= 'Anime_Review_Index'),
    path('delete/<int:Review_id>/review', DeleteAnimeReview.as_view(), name= 'Anime_Review_Index'),
    path('posts/',PostIndex.as_view() , name= 'Post_Index'),
    path('post/<int:Post_id>/', PostDetail.as_view(), name= 'Post_Detail'),
    path('post/<int:Post_id>/comment/', PostCommentIndex.as_view(), name= 'Anime_Review_Index'),
    path('delete/<int:Comment_id>/comment', DeletePostComment.as_view(), name= 'Anime_Review_Index'),
    path('addpost/<int:Post_id>/tofavorit/', AddPostToFavorit.as_view(), name= 'Add_Post_To_Favorit'),
    path('removepost/<int:Favorit_id>/fromfavorit/', RemovePostFromFavorit.as_view(), name= 'Remove_Post_From_Favorit'),
    path('mypostfavoritlist/',MyPostToFavoritList.as_view() , name= 'My_Post_Favorit_List'),

] 