from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Anime , Profile , Post , User
from .serializers import Animeserializer , Profileserializer , Postserializer, Userserializer 
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
            return Response({"error":" please provide a username,email and password "},status =status.HTTP_400_BAD_REQUEST)
 
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

    
class DeleteUser(APIView):
     # ---------------Delete user---------------
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        user = User.objects.get(id = request.user)
        user.delete()
        return Response()



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
            serializer = Profileserializer(queryset, data= request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status =status.HTTP_200_OK )
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)
            


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
               serializer.save()
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
            queryset.delete()
            return Response({'message': f'Anime {Anime_id} has been deleted !!! '},status =status.HTTP_204_NO_CONTENT )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)


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
               serializer.save()
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
            queryset.delete()
            return Response({'message': f'Post {Post_id} has been deleted !!! '},status =status.HTTP_204_NO_CONTENT )
        except Exception as error: 
            return Response({'error':str(error)},status =status.HTTP_500_INTERNAL_SERVER_ERROR)

