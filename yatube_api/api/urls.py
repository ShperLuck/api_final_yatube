from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),  # Маршруты для ViewSet'ов
    path('v1/api-token-auth/', obtain_auth_token, name='api-token-auth'),  # Эндпоинт для получения токена
    path('v1/', include('djoser.urls')),  # Дополнительные маршруты  djoser
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
]
