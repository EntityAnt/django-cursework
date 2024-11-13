from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.services import email_verification
from users.views import UserCreateView, UserLoginView, EmailConfirmationView, PasswordRecoveryView, UserDetailView, \
    UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('email-confirmation/', EmailConfirmationView.as_view(), name='email_confirmation'),
    path('password-recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
]
