#!/bin/bash

# Применение миграций
python manage.py makemigrations
python manage.py migrate

# Создание суперпользователя, если не существует
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" \
| python manage.py shell

# Запуск сервера
python manage.py runserver 0.0.0.0:8000
