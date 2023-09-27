from django.urls import path, include
from account.views import (
    UserLoginView, 
    UserRegistrationView, 
    UserLogoutView, 
    UserProfileView
)
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "account"

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),  # Add this line for logout
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
]
