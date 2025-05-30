from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet,
)

# Инициализация роутера
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_pk>\d+)/comments', CommentViewSet, basename='comments')

# URL-шаблоны
urlpatterns = [
    # Маршруты роутера
    path('v1/', include(router.urls)),
    # JWT-эндпоинты через Djoser
    path('v1/auth/', include('djoser.urls.jwt')),  # /jwt/create/, /jwt/refresh/, /jwt/verify/
]
