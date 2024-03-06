from rest_framework import routers
from .views import LogPostView, LogProfileView

router = routers.DefaultRouter()
router.register('post_views', LogPostView)
router.register('profile_views', LogProfileView)


# URLConf
urlpatterns = router.urls
