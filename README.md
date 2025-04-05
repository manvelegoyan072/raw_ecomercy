
## Установка
1. Клонируйте репозиторий:

   git clone <repository_url>
   cd raw_api
2. Установите зависимости:
   pip install -r requirements.txt
3. Примените миграции:
   python manage.py makemigrations или python manage.py makemigrations accounts products cart orders
   python manage.py migrate
4. Запустите сервер:
   python manage.py runserver
5. Создай админа
   python manage.py createsuperuser

## Запуск в Docker
   docker build -t raw_ecommercy .
   docker run -p 8000:8000 raw_ecommercy


