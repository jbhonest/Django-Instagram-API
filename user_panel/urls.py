from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import FollowViewSet, UserProfileViewSet, UserRegistrationViewSet


router = routers.DefaultRouter()
router.register('follow', FollowViewSet)
router.register('profile', UserProfileViewSet, basename='userprofile')
router.register('register', UserRegistrationViewSet)


# URLConf
urlpatterns = router.urls

urlpatterns += [
    path('login/', obtain_auth_token, name='login'),
]
