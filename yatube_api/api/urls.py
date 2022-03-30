from django.urls import include, path
from rest_framework import routers

from .views import (
    CommentViewSet,
    FollowListCreateViewSet,
    GroupViewSet,
    PostViewSet,
)

router = routers.DefaultRouter()
router.register(
    r"v1/posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
router.register(r"v1/follow", FollowListCreateViewSet, basename="follow")
router.register(r"v1/groups", GroupViewSet)
router.register(r"v1/posts", PostViewSet)


urlpatterns = [
    path("v1/auth/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
urlpatterns += router.urls
