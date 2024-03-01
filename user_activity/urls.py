from rest_framework import routers
from .views import CommentViewSet

router = routers.DefaultRouter()
router.register('comments', CommentViewSet)

# URLConf
urlpatterns = router.urls
