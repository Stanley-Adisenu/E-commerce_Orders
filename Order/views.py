from django.shortcuts import render
from .models import OrderItems,Orders,User
from .serializers import OrderSerializer,OrderItemsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
    
# Get and post an order
@api_view(['GET','POST'])
def order_list(request):
    if request.method == 'GET':
        status = Orders.objects.all()
        serializer = OrderSerializer(status,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message":"An error occured"})

# get a specific order    
@api_view(['GET','PUT','DELETE'])
def order_update(request,pk):
    if request.method == 'GET':
        order_items = get_object_or_404(Orders,id=pk)
        serializer = OrderSerializer(order_items)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        order_items = get_object_or_404(Orders,id=pk)
        serializer = OrderSerializer(order_items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order_items = get_object_or_404(Orders,id=pk)
        order_items.status = 'cancelled'
        order_items.save()
        serializer = OrderSerializer(order_items)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    

    
# get order items
@api_view(['GET'])
def order_items_list(request):
    if request.method == 'GET':
        order_items = OrderItems.objects.all()
        serializer = OrderItemsSerializer(order_items,many=True)
        return Response(serializer.data)
    

# get a users order items 
@api_view(['GET'])
def user_orders(request,pk):
    if request.method == 'GET':
        user = get_object_or_404(User, id=pk)
        orders = Orders.objects.filter(user=user)
        order_items = OrderItems.objects.filter(order_id__in=orders)
        serializer = OrderItemsSerializer(order_items,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
