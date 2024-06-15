from rest_framework import serializers
from .models import Saved
from product.serializers import ProductSerializer


class SavedSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product = ProductSerializer()

    class Meta:
        model = Saved
        fields = ['id', 'product', 'user']
    

class SavedCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Saved
        fields = ['id', 'product', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        saved = Saved.objects.create(**validated_data)
        return saved