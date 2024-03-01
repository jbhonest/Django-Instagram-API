from rest_framework import routers
from .views import PostViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('images', ImageViewSet)

# URLConf
urlpatterns = router.urls
