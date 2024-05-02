
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer

class AccountsView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']

            # username과 email 중복 체크
            if User.objects.filter(username=username).exists():
                return Response({"error": "이미 사용 중인 이름인데...."}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=email).exists():
                return Response({"error": "이미 사용 중인 이메일인데...."}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class signupView(APIView):
    permission_classes = [AllowAny] #접근 권한
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            
            refresh_token = RefreshToken.for_user(user)
            data = {
                'user_id': user.id,
                'access_token': str(refresh_token.access_token),
                'refresh_token': str(refresh_token)
            }
            
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "아이디 및 비밀번호가 이상한데요?"}, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        logout(request)
        return Response({"message": "로그아웃 인가?"}, status=status.HTTP_200_OK)

class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, username):
        user = get_object_or_404(CustomUser, username=username)

        # 인증된 사용자가 프로필의 소유자인지 확인
        if request.user != user:
            return Response({"error": "권한 읍서요"}, status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            # 이메일 중복 확인
            new_email = serializer.validated_data.get('email')
            if new_email and CustomUser.objects.exclude(pk=user.pk).filter(email=new_email).exists():
                return Response({"error": "이미 존재한 이메일이에요."}, status=status.HTTP_400_BAD_REQUEST)

            # 사용자명(ID)
            new_username = serializer.validated_data.get('username')
            if new_username and CustomUser.objects.exclude(pk=user.pk).filter(username=new_username).exists():
                return Response({"error": "이미 존재한 아이디입니당."}, status=status.HTTP_400_BAD_REQUEST)
            
            # 이름
            new_name = serializer.validated_data.get('name')
            if new_name and CustomUser.objects.exclude(pk=user.pk).filter(name=new_name).exists():
                return Response({"error": "이미 존재한 이름입니당."}, status=status.HTTP_400_BAD_REQUEST)
            
            # 닉네임
            new_nickname = serializer.validated_data.get('nickname')
            if new_nickname and CustomUser.objects.exclude(pk=user.pk).filter(name=new_nickname).exists():
                return Response({"error": "이미 존재한 닉네임입니당."}, status=status.HTTP_400_BAD_REQUEST)
            
            # 생일
            new_birthday = serializer.validated_data.get('birthday')
            if new_birthday and CustomUser.objects.exclude(pk=user.pk).filter(birthday=new_birthday).exists():
                return Response(serializer.data, status=status.HTTP_200_OK)
            

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)