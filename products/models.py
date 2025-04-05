from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  # Название категории
    slug = models.SlugField(unique=True)     # Уникальный slug для URL

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)             # Название товара
    description = models.TextField()                    # Описание
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Изображение
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    stock = models.PositiveIntegerField()               # Количество на складе
    specifications = models.JSONField(blank=True, null=True)  # Характеристики в формате JSON
    categories = models.ManyToManyField(Category, related_name='products')  # Связь с категориями

    def __str__(self):
        return self.name