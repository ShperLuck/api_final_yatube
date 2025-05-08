from django.urls import path, include  # Импорт маршрутов Django
from rest_framework.routers import DefaultRouter  # Роутер DRF для ViewSet'ов
from rest_framework_simplejwt.views import TokenObtainPairView  # Получение JWT токена

# Импорт кастомных ViewSet'ов и JWT обработчиков из текущего приложения
from .views import (
    PostViewSet,       # ViewSet для постов
    CommentViewSet,    # ViewSet для комментариев
    GroupViewSet,      # ViewSet для групп
    FollowViewSet,     # ViewSet для подписок
    CustomTokenRefreshView,  # Кастомный refresh-токен
    CustomTokenVerifyView    # Кастомная проверка токена
)


# Роутер для ViewSet'ов
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('v1/', include(router.urls)),  # Автоматические маршруты для постов

    # JWT эндпоинты
    path('v1/jwt/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('v1/jwt/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='token-create'),

    # Комментарии к постам
    path('v1/posts/<int:post_pk>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='comment-list'),
    path('v1/posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='comment-detail'),

    # Подписки
    path('v1/follow/', FollowViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='follow'),

    # Группы
    path('v1/groups/',
         GroupViewSet.as_view({'get': 'list'}), name='group-list'),
    path('v1/groups/<int:pk>/',
         GroupViewSet.as_view({'get': 'retrieve'}), name='group-detail'),
]
