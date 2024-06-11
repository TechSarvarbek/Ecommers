from django.urls import path
from .views import UserRegistrationView, UserLoginView, VerifyEmail

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('verify/', VerifyEmail.as_view(), name='verify-email'),
]