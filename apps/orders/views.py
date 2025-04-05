from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import Cart, CartItem
from django.db import transaction

class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        cart = Cart.objects.get(user=request.user)
        if not cart.items.exists():
            return Response({'error': 'Корзина пуста'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            order = Order.objects.create(user=request.user, status='pending')
            total_price = 0
            for item in cart.items.all():
                order_item = OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
                total_price += item.quantity * item.product.price
                item.product.stock -= item.quantity
                item.product.save()
            order.total_price = total_price
            order.save()
            cart.items.all().delete()  # Очистка корзины
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)