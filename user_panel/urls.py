from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import FollowViewSet, UserProfileViewSet, UserViewSet, RegisterApi


router = routers.DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('users', UserViewSet, basename='user')
router.register('profile', UserProfileViewSet, basename='userprofile')


# URLConf
urlpatterns = router.urls

urlpatterns += [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterApi.as_view()),
]
