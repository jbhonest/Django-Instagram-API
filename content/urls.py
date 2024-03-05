from rest_framework import routers
from .views import PostViewSet, ImageViewSet, MentionViewSet, HashtagViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('images', ImageViewSet, basename='images')
router.register('hashtags', HashtagViewSet)
router.register('mentions', MentionViewSet)


# URLConf
urlpatterns = router.urls
