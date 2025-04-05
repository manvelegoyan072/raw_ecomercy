from django.urls import path
from .views import OrderViewSet

urlpatterns = [
    path('', OrderViewSet.as_view({'get': 'list'}), name='order_list'),          # Список заказов
    path('create/', OrderViewSet.as_view({'post': 'create'}), name='order_create'),  # Создание заказа
]