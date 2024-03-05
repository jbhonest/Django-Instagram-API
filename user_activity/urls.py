from rest_framework import routers
from .views import CommentViewSet, PostLikeViewSet

router = routers.DefaultRouter()
router.register('comments', CommentViewSet)
router.register('likes', PostLikeViewSet)

# URLConf
urlpatterns = router.urls
