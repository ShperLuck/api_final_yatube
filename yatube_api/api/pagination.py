from rest_framework.pagination import LimitOffsetPagination

# Кастомный класс пагинации, применет пагинацию только при наличии этих параметров limit и offset


class OptionalLimitOffsetPagination(LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        # Проверка на наличие параметров limit, offset в запросе
        if 'limit' in request.query_params and 'offset' in request.query_params:
            # + стандартная пагинация
            return super().paginate_queryset(queryset, request, view)
        # - без пагинаци
        return None
