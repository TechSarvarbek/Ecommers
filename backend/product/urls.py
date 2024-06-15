from django.urls import path
from .views import (
    MyProductListCreateAPIView, 
    MyProductRetrieveUpdateDestroyAPIView,
    ProductListApiView,
    ProductDetailApiView
)


urlpatterns = [
    path('products/', ProductListApiView.as_view(), name='products'),
    path('my-products/', MyProductListCreateAPIView.as_view(), name='product-list-create'),
    path('my-product/<int:pk>/', MyProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('detail/<int:id>/', ProductDetailApiView.as_view(), name='product-detail'),
]