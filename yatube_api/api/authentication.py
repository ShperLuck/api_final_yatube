# Импорт базовых сериализаторов для работы с JWT-токенами
# TokenVerifySerializer: для проверки валидности токенов
# TokenRefreshSerializer: для обновления access-токенов

# Импорт исключения AuthenticationFailed для обработки ошибок аутентификации

# Импорт классов токенов
# RefreshToken: для создания и обработки refresh-токенов
# TokenError: для обработки ошибок, связанных с токенами
# UntypedToken: для проверки токенов без строгой типизации

from rest_framework_simplejwt.serializers import (
    TokenVerifySerializer, TokenRefreshSerializer
)
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import (
    RefreshToken, TokenError, UntypedToken
)

# Ручной сериализатор JWT-токена - не получилось сделать автоматизацию готовыми эндпоинтами Djoser


class CustomTokenVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs):
        try:
            # Проверяет валидность токена
            UntypedToken(attrs["token"])
        except TokenError:
            # Выбрасывает ошибку, если токен недействителен или истек
            raise AuthenticationFailed(
                detail="Token is invalid or expired",
                code="token_not_valid"
            )
        return {}

# Вручную пришлось делать сериализатор для обновления вот этой JWT-токена


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        refresh = attrs['refresh']  # Получает refresh-токен из данных

        try:
            # Создает новый access-токен на основе refresh-токена
            token = RefreshToken(refresh)
            # Возвращает новый access-токен
            data = {"access": str(token.access_token)}
            return data
        except TokenError:
            # Выбрасывает ошибку, если refresh-токен недействителен или истек
            raise AuthenticationFailed(
                detail="Token is invalid or expired",
                code="token_not_valid"
            )
