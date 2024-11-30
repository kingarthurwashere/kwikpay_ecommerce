from rest_framework import serializers
from .models import Cart, Order, Payment

class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'product_name', 'product_price', 'quantity', 'total_price']


class OrderSerializer(serializers.ModelSerializer):
    cart_items = CartSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'cart_items', 'total_price', 'status', 'created_at']


class PaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.ReadOnlyField(source='order.id')

    class Meta:
        model = Payment
        fields = ['id', 'order_id', 'payment_link', 'status', 'created_at']
