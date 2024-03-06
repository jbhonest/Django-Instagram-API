from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import FollowViewSet, UserProfileViewSet, PublicProfilesViewSet, RegisterApi, PublicFollowViewSet, FollowingUserProfileViewSet


router = routers.DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('profile', UserProfileViewSet, basename='userprofile')
# router.register('following_profiles', FollowingUserProfileViewSet, basename='followinguserprofiles')
# router.register('public_follow', PublicFollowViewSet, basename='publicfollow')
router.register('public_profiles', PublicProfilesViewSet)


# URLConf
urlpatterns = router.urls

urlpatterns += [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterApi.as_view()),
]
