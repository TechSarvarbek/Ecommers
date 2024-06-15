from django.urls import path
from .views import ProfileView, ProfileUpdateView, ChangePasswordView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('change/password/', ChangePasswordView.as_view(), name='change-password'),
]