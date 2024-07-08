# book/views.py

from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsAdminUser, IsAssistantUser, IsAdminOrAssistant
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('books').all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'id': user.id,
            'username': user.username,
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register(request):
#     serializer = UserSerializer(data=request.data)
    
#     if serializer.is_valid():
#         user = serializer.save()
#         refresh=RefreshToken.for_user(user)
#         return Response({
#         'id': user.id,
#         'username': user.username,
#         'access': str(refresh.access_token),
#         'refresh': str(refresh)
#     }, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    





@api_view(['POST'])
@permission_classes([AllowAny])
def logout(request):
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    



class AdminView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        return Response({"message": "Hello, Admin!"})

class AdminOrAssistantView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrAssistant]

    def get(self, request):
        return Response({"message": "Hello, Admin or Assistant!"})

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, User!"})    


class GodLevelView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
         return Response("index.html")



        
        
       