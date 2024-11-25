from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, UserProfileView, UpdateProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile'),
]
