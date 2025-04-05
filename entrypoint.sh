#!/bin/bash


export $(grep -v '^#' .env | xargs)

# Применение миграций
python manage.py makemigrations
python manage.py migrate

# Создание суперпользователя, если не существует
echo "
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
" | python manage.py shell

# Запуск сервера
python manage.py runserver 0.0.0.0:8000
