from rest_framework import serializers
from .models import Category, MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator
import bleach

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    def validate_title(self, value):
        return bleach.clean(value)  # Sanitize the 'title' field using bleach

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'feature', 'category']

class UserCartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True  # Make the user field read-only
    )
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='menuitem.price', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'unit_price', 'quantity', 'price']
        validators = [
            UniqueTogetherValidator(
                queryset=Cart.objects.all(),
                fields=('user', 'menuitem')
            )
        ]
        extra_kwargs = {
            'price': {'read_only': True}  # 'price' field should be read-only
        }



class UserOrdersItemSerializer(serializers.ModelSerializer):  # Updated to UserOrdersItemSerializer
    class Meta:
        model = OrderItem
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']

class UserOrdersSerializer(serializers.ModelSerializer):  # Updated to UserOrdersSerializer
    orderitem = UserOrdersItemSerializer(many=True, read_only=True)  # Nested serializer for order items

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'date', 'total', 'orderitem']

class UserSerializer(serializers.ModelSerializer):  # Corrected the name to UserSerializer
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
