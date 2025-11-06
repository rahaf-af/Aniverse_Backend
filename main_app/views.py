from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User , Profile, Anime , Review ,AnimeFavorit, Post , PostComment, PostFavorit , Contact
from .serializers import  Userserializer, Profileserializer, Animeserializer, AnimeFavoritserializer, Reviewserializer, Postserializer, PostFavoritserializer, PostCommentserializer, Contacteserializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)


# Create your views here.
# ---------------User---------------
class Signup(APIView):
    # ---------------Create user---------------
    permission_classes = [AllowAny]
    def post(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not first_name or not last_name or not username or not email or not password:
            return Response({"error":" please provide your first name,last_name, username,email and password "},status =status.HTTP_400_BAD_REQUEST)
 
        if User.objects.filter(username = username).exists():
            return Response({"error":"user Already exists"},status =status.HTTP_400_BAD_REQUEST)
        
        try:
            serializer = Userserializer(data= request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status =status.HTTP_201_CREATED )
            return Response({'message': f'user {username} has been created !!! '},serializer.errors,status =status.HTTP_400_BAD_REQUEST )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR )

    
class Handeluser(APIView):
     # ---------------Delete user---------------
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        user = User.objects.get(id = request.user)
        user.delete()
        return Response()
    # ---------------Get user info---------------
    def get(self, request):
        queryset = get_object_or_404(User,id=request.user.id)
        serializer = Userserializer(queryset)
        return Response(serializer.data)
    


# ---------------Profile---------------
class ProfileDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # ---------------Profile Detail---------------
    def get(self, request, Profile_id):
        queryset = get_object_or_404(Profile,id=Profile_id)
        serializer = Profileserializer(queryset)
        return Response(serializer.data)
    
    # ---------------Update Profile---------------
    def put(self, request, Profile_id):
        try:
            queryset = get_object_or_404(Profile,id=Profile_id)
            if request.user != queryset.user:
                return Response({'message': 'You do not have permission to edit other users profiles.'},serializer.errors,status =status.HTTP_403_FORBIDDEN )
            serializer = Profileserializer(queryset, data= request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status =status.HTTP_200_OK )
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class MyProfile(APIView):
    permission_classes = [IsAuthenticated]
    # ---------------My Profile Detail---------------
    def get(self, request):
        queryset = get_object_or_404(Profile,user=request.user)
        serializer = Profileserializer(queryset)
        return Response(serializer.data)

class Contactus(APIView):
    permission_classes = [IsAuthenticated]
    # ---------------Create Contactus---------------
    def post(self, request):
        try:
            serializer = Contacteserializer(data= request.data)
            if serializer.is_valid():
               serializer.save(user= request.user)
               return Response(serializer.data,status =status.HTTP_201_CREATED )
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR )
        
class Homeanime(APIView):
    permission_classes = [AllowAny]
    # ---------------Read Last 3 Anime---------------
    def get(self, request ):
        queryset = Anime.objects.order_by('-created_at')[:5]
        serializer = Animeserializer(queryset, many=True)
        return Response(serializer.data)
    
class Homeposts(APIView):
    permission_classes = [AllowAny]
    # ---------------Read Last 3 Post---------------
    def get(self, request ):
        queryset = Post.objects.order_by('-created_at')[:5]
        serializer = Postserializer(queryset, many=True)
        return Response(serializer.data)
    


# ---------------Anime---------------
class AnimeIndex(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # ---------------Read Anime---------------
    def get(self, request ):
        queryset = Anime.objects.all()
        serializer = Animeserializer(queryset, many=True)
        return Response(serializer.data)
    
    # ---------------Create Anime---------------
    def post(self, request):
        try:
            serializer = Animeserializer(data= request.data)
            if serializer.is_valid():
               serializer.save(publisher= request.user)
               return Response(serializer.data,status =status.HTTP_201_CREATED )
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR )

class AnimeDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # ---------------Anime Detail---------------
    def get(self, request, Anime_id):
        queryset = get_object_or_404(Anime,id=Anime_id)
        serializer = Animeserializer(queryset)
        return Response(serializer.data)
    
    # ---------------Update Anime---------------
    def put(self, request, Anime_id):
        try:
            queryset = get_object_or_404(Anime,id=Anime_id)
            if request.user != queryset.publisher:
                return Response({'message': 'You do not have permission to edit other users Anime.'},serializer.errors,status =status.HTTP_403_FORBIDDEN )
            serializer = Animeserializer(queryset, data= request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status =status.HTTP_200_OK )
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # ---------------Delete Anime---------------
    def delete(self, request, Anime_id):
        try:
            queryset = get_object_or_404(Anime,id=Anime_id)
            if request.user != queryset.user:
                return Response({'message': 'You do not have permission to delete other users Anime.'},status =status.HTTP_403_FORBIDDEN )
            queryset.delete()
            return Response({'message': f'Anime {Anime_id} has been deleted !!! '},status =status.HTTP_204_NO_CONTENT )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)



# ---------------Interact with Anime---------------
class  AnimeReviewIndex(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # ---------------Read Anime Review---------------
    def get(self, request, Anime_id):
        queryset = Review.objects.filter(anime=Anime_id)
        serializer = Reviewserializer(queryset, many=True)
        return Response(serializer.data)
    
    # ---------------Create Anime Review---------------
    def post(self, request, Anime_id):
        try:
            serializer = Reviewserializer(data = request.data)
            if serializer.is_valid():
                anime = get_object_or_404(Anime,id=Anime_id)
                serializer.save(anime=anime,user=request.user)
                queryset = Review.objects.filter(anime=Anime_id)
                serializer = Reviewserializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR )
        
class DeleteAnimeReview(APIView):
    permission_classes = [IsAuthenticated]
# ---------------Delete Anime Review---------------
    def delete(self, request, Review_id):
        try:
            queryset = get_object_or_404(Review,id=Review_id)
            if request.user != queryset.user:
                return Response({'message': 'You do not have permission to delete other users reviews.'},status =status.HTTP_403_FORBIDDEN )
            queryset.delete()
            return Response({'message': f'Review {Review_id} has been deleted !!! '},status =status.HTTP_204_NO_CONTENT )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AddAnimeToFavorit(APIView):
    # ---------------Add Anime To Favorit---------------
    def post(self, request, Anime_id):
        try:
            serializer = AnimeFavoritserializer(data = request.data)
            if serializer.is_valid():
                anime = get_object_or_404(Anime,id=Anime_id)
                serializer.save(anime=anime,user=request.user)
                queryset = AnimeFavorit.objects.filter(anime=Anime_id)
                serializer = AnimeFavoritserializer(queryset, many=True)
                return Response({'message': f'Anime {Anime_id} has been added to your favorit list !! ', 'data':serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR )

class RemoveAnimeFromFavorit(APIView):
    # ---------------Remove Anime From Favorit---------------
    def delete(self, request, Favorit_id):
        try:
            queryset = get_object_or_404(AnimeFavorit,id=Favorit_id, user=request.user)
            if request.user != queryset.user:
                return Response({'message': 'You do not have permission to remove Anime From other users Favorit list !!!.'},status =status.HTTP_403_FORBIDDEN )
            queryset.delete()
            return Response({'message': f'Anime has been Removed from Favorit list !!! '},status =status.HTTP_204_NO_CONTENT )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)

class MyAnimeToFavoritList(APIView):
    permission_classes = [IsAuthenticated]
    # ---------------Read User Favorit List---------------
    def get(self, request):
        queryset = AnimeFavorit.objects.filter(user=request.user)
        serializer = AnimeFavoritserializer(queryset, many=True)
        return Response(serializer.data)
        

# ---------------Post---------------
class PostIndex(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # ---------------Read Post---------------
    def get(self, request ):
        queryset = Post.objects.all()
        serializer = Postserializer(queryset, many=True)
        return Response(serializer.data)
    
    # ---------------Create Post---------------
    def post(self, request):
        try:
            serializer = Postserializer(data= request.data)
            if serializer.is_valid():
               serializer.save(auther= request.user)
               return Response(serializer.data,status =status.HTTP_201_CREATED )
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR )

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # ---------------Post Detail---------------
    def get(self, request, Post_id):
        queryset = get_object_or_404(Post,id=Post_id)
        serializer = Postserializer(queryset)
        return Response(serializer.data)
    
    # ---------------Update Post---------------
    def put(self, request, Post_id):
        try:
            queryset = get_object_or_404(Post,id=Post_id)
            if request.user != queryset.auther:
                return Response({'message': 'You do not have permission to edit other users posts.'},serializer.errors,status =status.HTTP_403_FORBIDDEN )
            serializer = Postserializer(queryset, data= request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status =status.HTTP_200_OK )
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # ---------------Delete Post---------------
    def delete(self, request, Post_id):
        try:
            queryset = get_object_or_404(Post,id=Post_id)
            if request.user != queryset.auther:
                return Response({'message': 'You do not have permission to delete other users posts.'},status =status.HTTP_403_FORBIDDEN )
            queryset.delete()
            return Response({'message': f'Post {Post_id} has been deleted !!! '},status =status.HTTP_204_NO_CONTENT )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # ---------------Interact with post---------------
class  PostCommentIndex(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # ---------------Read Post Comment---------------
    def get(self, request, Post_id):
        queryset = PostComment.objects.filter(post=Post_id)
        serializer = PostCommentserializer(queryset, many=True)
        return Response(serializer.data)
    
    # ---------------add Post Comment---------------
    def post(self, request, Post_id):
        try:
            serializer = PostCommentserializer(data = request.data)
            if serializer.is_valid():
                post = get_object_or_404(Post,id=Post_id)
                serializer.save(post=post,user=request.user)
                queryset = PostComment.objects.filter(post=Post_id)
                serializer = PostCommentserializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR )
        
class DeletePostComment(APIView):
    permission_classes =[IsAuthenticated]
# ---------------Delete Post Comment---------------
    def delete(self, request, Comment_id):
        try:
            queryset = get_object_or_404(PostComment,id=Comment_id)
            if request.user != queryset.user:
                return Response({'message': 'You do not have permission to delete other users reviews.'},status =status.HTTP_403_FORBIDDEN )
            queryset.delete()
            return Response({'message': f'Comment {Comment_id} has been deleted !!! '},status =status.HTTP_204_NO_CONTENT )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AddPostToFavorit(APIView):
    permission_classes = [IsAuthenticated]
    # ---------------Add Post To Favorit---------------
    def post(self, request, Post_id):
        try:
            serializer = PostFavoritserializer(data = request.data)
            if serializer.is_valid():
                post = get_object_or_404(Post,id=Post_id)
                serializer.save(post=post,user=request.user)
                queryset = PostFavorit.objects.filter(post=Post_id)
                serializer = PostFavoritserializer(queryset, many=True)
                return Response({'message': f'Post {Post_id} has been added to your favorit list !! ', 'data':serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR )

class RemovePostFromFavorit(APIView):
    permission_classes = [IsAuthenticated]
    # ---------------Remove Post From Favorit---------------
    def delete(self, request, Favorit_id):
        try:
            queryset = get_object_or_404(PostFavorit,id=Favorit_id, user=request.user)
            if request.user != queryset.user:
                return Response({'message': 'You do not have permission to remove Post From other users Favorit list !!!.'},status =status.HTTP_403_FORBIDDEN )
            queryset.delete()
            return Response({'message': f'Post has been Removed from Favorit list !!! '},status =status.HTTP_204_NO_CONTENT )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)

class MyPostToFavoritList(APIView):
    permission_classes = [IsAuthenticated]
    # ---------------Read User Favorit List---------------
    def get(self, request):
        queryset = PostFavorit.objects.filter(user=request.user)
        serializer = PostFavoritserializer(queryset, many=True)
        return Response(serializer.data)
