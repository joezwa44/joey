from .models import OrderItem
from rest_framework import serializers


class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'order',
            'product',
            'qty'
        ]
        read_only_fields = [
            'order'
        ]