from rest_framework import routers
from .views import PostViewSet, ImageViewSet, MentionViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('images', ImageViewSet)
router.register('mentions', MentionViewSet)

# URLConf
urlpatterns = router.urls
