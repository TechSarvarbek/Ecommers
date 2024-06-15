from django.urls import path
from .views import ProductListApiView


urlpatterns = [
    path('filter/', ProductListApiView.as_view(), name='product-filter'),
]