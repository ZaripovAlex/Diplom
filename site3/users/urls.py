from django.urls import path, include

from . import views
from .views import  CreateUser

app_name = "users"

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    # path('reg/', views.user_registration, name='reg'),
    path('signup/', CreateUser.as_view(), name='reg'),
]
