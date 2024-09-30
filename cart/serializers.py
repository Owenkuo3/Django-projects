from rest_framework import serializers
from .models import cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ['id', 'user', 'product', 'quantity', 'added_at']
        read_only_fields = ['id', 'added_at', 'user']
        
    def validate_product(self, value):
        if not Product.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("此產品不存在。")
        return value

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("數量必須大於 0。")
        product = self.initial_data.get('product')
        if product and value > Product.objects.get(id=product).stock:
            raise serializers.ValidationError("數量超過庫存。")
        return value