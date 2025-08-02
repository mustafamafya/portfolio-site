from django.urls import path
from .views import profile , login_user , register,update_profile,delete_profile # Import the profile view from views.py
from . import views
from django.urls import path
urlpatterns = [
    
    path('', profile, name='profile' ),  # URL pattern for the user profile page
    path('login/', login_user, name='login'),  # URL pattern for the login page
    path('register/', register, name='register'),  # URL pattern for the registration page
    path('logout/', views.logout_page, name='logout'),  # URL pattern for the logout action
    path('update-profile/', update_profile, name='update_profile'), # URL pattern for updating the profile
    path('delete-profile/', delete_profile, name='delete_profile'),  # URL pattern for deleting the profile
    ]

   

