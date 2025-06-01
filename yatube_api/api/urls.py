from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'v1/posts', PostViewSet, basename='posts')
router.register(r'v1/groups', GroupViewSet, basename='groups')
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('verify_valid_token/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
