from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Category

class ProductTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Электроника', slug='electronics')
        self.product = Product.objects.create(
            name='Смартфон',
            description='Современный смартфон',
            price=999.99,
            stock=10,
            specifications={'color': 'black', 'memory': '128GB'}
        )
        self.product.categories.add(self.category)

    def test_get_products(self):
        response = self.client.get('/raw_api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Смартфон')