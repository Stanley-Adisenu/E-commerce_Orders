from rest_framework import serializers
from .models import OrderItems,Orders,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name']



class OrderSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Orders
        fields = ['id','status','user','total_amount','created_at','updated_at']

class OrderItemsSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer()
    class Meta:
        model = OrderItems
        fields = ['id','order_id','listings','quantity','price','created_at','updated_at']
