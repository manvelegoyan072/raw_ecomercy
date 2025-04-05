from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from products.models import Product, Category

class CartTestCase(TestCase):
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

    def test_add_to_cart(self):
        response = self.client.post('/raw_api/cart/add/', {'product_id': self.product.id, 'quantity': 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['quantity'], 2)

    def test_get_cart(self):
        self.client.post('/raw_api/cart/add/', {'product_id': self.product.id, 'quantity': 1})
        response = self.client.get('/raw_api/cart/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)