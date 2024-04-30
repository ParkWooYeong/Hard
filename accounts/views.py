from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer

@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "로그인을 성공하셨네요?"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "이게 왜 안될까요?"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return Response({"message": "로그아웃이 되었다!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request, username):
    user = request.user
    if user.username == username:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response({"message": "이게 너의 프로필이다"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    if request.user.is_staff:
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "님 이거 볼수있는 권한이 없음"}, status=status.HTTP_403_FORBIDDEN)