from django.db.models import Q
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from product.models import Product
from product.serializers import ProductSerializer


class ProductListApiView(APIView):
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get(self, request):
        # Retrieve query parameters
        search_query = request.query_params.get('search')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        deliver = request.query_params.get('deliver')

        # Apply filters
        products = Product.objects.all()

        if search_query:
            products = products.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

        if deliver:
            products = products.filter(deliver=True)

        # Apply pagination
        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)