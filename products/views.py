from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Чтение для всех, запись для авторизованных
    pagination_class = PageNumberPagination           # Пагинация
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]  # Фильтры и сортировка
    filterset_fields = ['categories', 'price']        # Фильтрация по категориям и цене
    ordering_fields = ['price', 'name']               # Сортировка по цене и названию

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]