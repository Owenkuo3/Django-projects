from rest_framework import serializers
from .models import cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ['id', 'user', 'product', 'quantity', 'added_at']
        read_only_fields = ['id', 'added_at', 'user']