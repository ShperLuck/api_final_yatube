from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from .permissions import IsAuthorOrReadOnly, FollowPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
)
from posts.models import Post, Comment, Group, Follow
from .pagination import OptionalLimitOffsetPagination
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView
from .authentication import (
    CustomTokenVerifySerializer, CustomTokenRefreshSerializer
)

# ViewSet для работы с постами


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  # Сериализатор для постов
    authentication_classes = [JWTAuthentication]  # Аутентификация через JWT
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = OptionalLimitOffsetPagination

    # Сохраняет пост с текущим пользователем как автором
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ViewSet для работы с комментариями


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer  # Сериализатор для комментариев
    authentication_classes = [JWTAuthentication]  # Аутентификация через JWT
    # Только автор может редактировать
    permission_classes = [IsAuthorOrReadOnly]

    # Возвращает комментарии для конкретного поста
    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        # Существование поста
        post = get_object_or_404(Post, pk=post_id)
        # Фильтр
        return Comment.objects.filter(post=post)

    # Сохраняет комментарий с текущим пользователем и привязкой к посту
    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')

        post = get_object_or_404(Post, pk=post_id)

        serializer.save(author=self.request.user, post=post)

# ViewSet для работы с группами


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer  # Сериализатор для групп
    authentication_classes = [JWTAuthentication]  # Аутентификация через JWT

    # Запрещает создание групп через API
    def create(self, serializer):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# ViewSet для работы с подписками


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer  # Сериализатор для подписок
    authentication_classes = [JWTAuthentication]  # Аутентификация через JWT
    # Доступ только аутентифицированным
    permission_classes = [FollowPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    # Возвращает подписки текущего пользователя
    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    # Сохраняет подписку с текущим пользователем
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Кастом представления JWT-токена


class CustomTokenVerifyView(TokenVerifyView):
    serializer_class = CustomTokenVerifySerializer

# Кастом представления обновления JWT-токена


class CustomTokenRefreshView(TokenRefreshView):

    serializer_class = CustomTokenRefreshSerializer
