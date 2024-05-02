from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AccountsView, signupView, LoginView, LogoutView, ProfileView, ProfileUpdateView

app_name = "accounts"

urlpatterns = [
    path('', AccountsView.as_view(), name='user_list'),
    path('signup/', signupView.as_view(), name='user_signup'),
    path('login/',LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('<str:username>/', ProfileView.as_view(), name='user_profile'),
    path('<str:username>/update/', ProfileUpdateView.as_view(), name='user_profile_update'),
    path("admin/signup/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]