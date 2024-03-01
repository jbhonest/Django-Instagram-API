from rest_framework import routers
from .views import CommentViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)

# URLConf
urlpatterns = router.urls
