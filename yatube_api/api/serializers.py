from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Post, Group, Follow, User

# Сериализатор для модели Post


class PostSerializer(serializers.ModelSerializer):
    # Поле author отображает имя пользователя, только для чтения
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        required = ('text',)
        model = Post

# Сериализатор для модели Comment


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        required = ('text',)
        read_only_fields = ('author', 'post')
        model = Comment

# Сериализатор для модели Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group

# Сериализатор для модели Follow


class FollowSerializer(serializers.ModelSerializer):
    # Поле user отображает имя пользователя, только для чтения
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    # Поле following позволяет выбрать пользователя для подписки
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        read_only_fields = ('user',)
        required = ('user', 'following')
        model = Follow

    # Валидация данных
    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        # Проверяет, что пользователь не подписывается на себя
        if user == following:
            raise serializers.ValidationError('You can\'t follow yourself.')
        # Проверяет, что подписка еще не существует
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                'You\'re already following this user.'
            )
        return data
