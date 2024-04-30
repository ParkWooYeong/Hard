from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

app_name = "accounts"

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('api/accounts/signup/', views.user_signup, name='user_signup'),
    path('api/accounts/login/', views.user_login, name='user_login'),
    path('api/accounts/logout/', views.user_logout, name='user_logout'),
    path('api/accounts/<str:username>/', views.user_profile, name='user_profile'),
    path("signup/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    
]