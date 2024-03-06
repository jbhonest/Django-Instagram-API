from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import FollowViewSet, UserAccountViewSet, PublicProfilesViewSet, RegisterApi, PublicFollowViewSet, FollowingProfilesViewSet, ProfileViewSet


router = routers.DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('account', UserAccountViewSet, basename='account')
router.register('profile', ProfileViewSet, basename='profile')
router.register('following_profiles', FollowingProfilesViewSet,
                basename='followinguserprofiles')
# router.register('public_follow', PublicFollowViewSet, basename='publicfollow')
router.register('public_profiles', PublicProfilesViewSet,
                basename='public_profiles')


# URLConf
urlpatterns = router.urls

urlpatterns += [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterApi.as_view()),
]
