from django.urls import path
from .views import SavedProductApiView


urlpatterns = [
    path('saveds/', SavedProductApiView.as_view(), name='saveds'),
]