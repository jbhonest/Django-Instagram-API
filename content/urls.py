from rest_framework import routers
from .views import PostViewSet, PostImageViewSet, StoryImageViewSet, MentionViewSet, HashtagViewSet, StoryViewSet, FollowingPostViewSet, FollowingStoryViewSet

router = routers.DefaultRouter()
router.register('following_posts', FollowingPostViewSet,
                basename='following_posts')
router.register('following_stories', FollowingStoryViewSet,
                basename='following_stories')
router.register('posts', PostViewSet, basename='posts')
router.register('post_images', PostImageViewSet, basename='post_images')
router.register('hashtags', HashtagViewSet, basename='hashtags')
router.register('mentions', MentionViewSet, basename='mentions')
router.register('stories', StoryViewSet, basename='stories')
router.register('story_images', StoryImageViewSet, basename='story_images')


# URLConf
urlpatterns = router.urls
