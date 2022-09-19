from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet, signup, token)
from django.urls import include, path
from rest_framework.routers import SimpleRouter

router_v1 = SimpleRouter()
router_v1.register('users', UserViewSet, basename='user')
router_v1.register(
    'categories',
    CategoryViewSet,
    basename='category'
)
router_v1.register('genres', GenreViewSet, basename='genre')
router_v1.register('titles', TitleViewSet, basename='title')
router_v1.register(
    r'titles/(?P<title_id>[1-9][0-9]*)/reviews',
    ReviewViewSet,
    basename='review'
)
router_v1.register(
    r'titles/(?P<title_id>[1-9][0-9]*)/reviews/'
    r'(?P<review_id>[1-9][0-9]*)/comments',
    CommentViewSet,
    basename='comment'
)
signup_token_urlpatterns = [
    path('auth/signup/', signup),
    path('auth/token/', token),
]
urlpatterns = [
    path('v1/', include(signup_token_urlpatterns)),
    path('v1/', include(router_v1.urls)),
]
