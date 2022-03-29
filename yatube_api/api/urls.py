from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowView, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"v1/posts", PostViewSet)
router.register(r"v1/groups", GroupViewSet)
router.register(
    r"v1/posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path("v1/auth/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
    path("v1/follow/", FollowView.as_view()),
]
urlpatterns += router.urls
