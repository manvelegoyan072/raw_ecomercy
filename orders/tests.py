from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from products.models import Product, Category
from cart.models import Cart, CartItem

class OrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='Электроника', slug='electronics')
        self.product = Product.objects.create(
            name='Смартфон',
            description='Современный смартфон',
            price=999.99,
            stock=10,
            specifications={'color': 'black', 'memory': '128GB'}
        )
        self.product.categories.add(self.category)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_create_order(self):
        response = self.client.post('/raw_api/orders/create/', {'address': 'Тестовый адрес'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['total_price'], '1999.98')  # 2 * 999.99

    def test_get_orders(self):
        self.client.post('/raw_api/orders/create/', {'address': 'Тестовый адрес'})
        response = self.client.get('/raw_api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)