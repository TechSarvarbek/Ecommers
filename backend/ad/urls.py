from django.urls import path
from .views import ads

urlpatterns = [
    path('ads/', ads, name='ad'),
]