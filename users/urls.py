from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, UserProfileView, UpdateProfileView, AdminCreateView, \
    CustomerListView, AdminDashboardView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('admin/create/', AdminCreateView.as_view(), name='create_admin'),
    path('admin/customers/', CustomerListView.as_view(), name='list_customers'),
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),

]
