from django.urls import path # This is the path function
from users.views import (
    UserListView, 
    UserCreateView,
    UserDeleteView, 
    UserProfileView,
    UserProfileUpdateView,
)


# This is the list of the routes

app_name = 'users'

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='user-profile'),
    path('<int:pk>/profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

]