from django.contrib import admin
from posts.models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', 'image')
    list_display_links = ('text', 'author')
    list_editable = ('group',)
    list_filter = ('pub_date', 'group')
    search_fields = ('text',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    list_display_links = ('title',)
    list_editable = ('slug',)
    search_fields = ('title', 'slug')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'post', 'created')
    list_editable = ('text',)
    list_display_links = ('pk',)
    list_filter = ('created', 'post')
    search_fields = ('text', 'author__username')
    empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following')
    list_filter = ('user', 'following')
    search_fields = ('user__username', 'following__username')
    empty_value_display = '-пусто-'
