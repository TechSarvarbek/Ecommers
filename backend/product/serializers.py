from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class MyProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'deliver', 'price', 'user', 'images']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        product = Product.objects.create(user=self.context['request'].user, **validated_data)
        for image_data in images_data:
            ProductImage.objects.create(product=product, image=image_data)
        return product


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'deliver', 'price', 'user', 'images',]