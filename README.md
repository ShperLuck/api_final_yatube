# api_final

Бойков Н.С. ИБАС-с-о-22-1

# Описание

API для социальной сети Yatube, разработанный с использованием Django REST Framework. Пользователи могут создавать посты, комментировать, подписываться на авторов и работать с JWT-авторизацией.

## Возможности

- Регистрация и авторизация пользователей (JWT)
- Создание и редактирование постов
- Комментирование постов
- Подписка на других пользователей
- Работа с группами и пагинацией
- Документация доступна по адресу `/redoc/`

## Установка

1. Клонирование репозитория

git clone https://github.com/ваш-юзернейм/api_final_yatube.git
cd api_final_yatube

2. Создание и активация вирт-окружения

python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate

3. Установка зависимости

pip install -r requirements.txt

4. Миграции и запуск сервера

python manage.py migrate
python manage.py runserver

## Примеры

1. Создать пост:

POST /api/v1/posts/
Authorization: Bearer <your_token>
{
  "text": "Мой пост",
  "group": 1
}

2. Добавить комментарий к посту:

POST /api/v1/posts/1/comments/
Authorization: Bearer <your_token>
{
  "text": " Готовый пост "
}