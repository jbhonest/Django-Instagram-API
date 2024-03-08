from rest_framework import routers
from .views import MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet, basename='messages')


# URLConf
urlpatterns = router.urls
