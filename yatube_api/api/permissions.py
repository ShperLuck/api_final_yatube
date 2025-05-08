from rest_framework import permissions

# Права только автору


class IsAuthorOrReadOnly(permissions.BasePermission):
    # Общие разрешения для запроса
    def has_permission(self, request, view):
        # Методы (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated

    # Иные дейсвтия
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        # Проверка на автора
        return obj.author == request.user

# Права авторизованным пользователям


class FollowPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated
