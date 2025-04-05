from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product

class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_cart(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def add_item(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        try:
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)

    def update_item(self, request, item_id):
        try:
            cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
            quantity = request.data.get('quantity')
            if quantity is not None:
                cart_item.quantity = int(quantity)
                cart_item.save()
                return Response(CartItemSerializer(cart_item).data)
            return Response({'error': 'Не указано количество'}, status=status.HTTP_400_BAD_REQUEST)
        except CartItem.DoesNotExist:
            return Response({'error': 'Элемент корзины не найден'}, status=status.HTTP_404_NOT_FOUND)

    def remove_item(self, request, item_id):
        try:
            cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({'error': 'Элемент корзины не найден'}, status=status.HTTP_404_NOT_FOUND)