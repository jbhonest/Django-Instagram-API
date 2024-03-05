from rest_framework import routers
from .views import CommentViewSet, PostLikeViewSet, StoryLikeViewSet

router = routers.DefaultRouter()
router.register('comments', CommentViewSet)
router.register('post_likes', PostLikeViewSet, basename='post_likes')
router.register('story_likes', StoryLikeViewSet, basename='story_likes')

# URLConf
urlpatterns = router.urls
