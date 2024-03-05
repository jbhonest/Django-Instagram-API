from rest_framework import routers
from .views import PostViewSet, ImageViewSet, MentionViewSet, HashtagViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('images', ImageViewSet, basename='images')
router.register('hashtags', HashtagViewSet, basename='hashtags')
router.register('mentions', MentionViewSet, basename='mentions')


# URLConf
urlpatterns = router.urls
