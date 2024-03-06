from rest_framework import routers
from .views import LogPostView

router = routers.DefaultRouter()
router.register('post_views', LogPostView)


# URLConf
urlpatterns = router.urls
