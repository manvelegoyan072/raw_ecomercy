from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)    # Эндпоинт для товаров
router.register(r'categories', CategoryViewSet) # Эндпоинт для категорий

urlpatterns = [
    path('', include(router.urls)),
]