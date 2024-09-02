from rest_framework import serializers 
from order.models import Wishlist , Basket_item, Basket
from product.api.serializers import ProductVersionSerializer

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer(many = True)

    class Meta:
        model = Wishlist
        fields = [
            'user' , 
            'product',
            'created_at',
        ]


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer(many=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = Basket_item
        fields = [
            'user',
            'product',
            'quantity',
            'subtotal',
        ]
        
    def get_subtotal(self, obj):
        return obj.get_subtotal()


class BasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True)  # Corrected to 'items'

    class Meta:
        model = Basket
        fields = [
            'user',
            'items',  # Corrected to 'items'
        ]
