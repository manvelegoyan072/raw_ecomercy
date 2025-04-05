from django.urls import path
from .views import CartViewSet

urlpatterns = [
    path('', CartViewSet.as_view({'get': 'get_cart'}), name='cart_detail'),           # Получение корзины
    path('add/', CartViewSet.as_view({'post': 'add_item'}), name='cart_add'),        # Добавление товара
    path('update/<int:item_id>/', CartViewSet.as_view({'put': 'update_item'}), name='cart_update'),  # Обновление количества
    path('remove/<int:item_id>/', CartViewSet.as_view({'delete': 'remove_item'}), name='cart_remove'),  # Удаление товара
]