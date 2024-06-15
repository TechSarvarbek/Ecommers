from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import MyProductSerializer, ProductSerializer

class MyProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MyProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
        

class MyProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


# products
class ProductListApiView(APIView):
    pagination_class = PageNumberPagination
    # Set the desired page size
    pagination_class.page_size = 50

    def get(self, request):
        products = Product.objects.all().order_by('-id')
        
        # Apply pagination
        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)
        
        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductDetailApiView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(serializer.data, status=404)