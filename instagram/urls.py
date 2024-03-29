from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from home.views import index

urlpatterns = [
    path('', index, name='index'),
    path(getattr(settings, 'ADMIN_URL'), admin.site.urls),
    path('content/', include('content.urls')),
    path('user_activity/', include('user_activity.urls')),
    path('user_panel/', include('user_panel.urls')),
    path('logger/', include('logger.urls')),
    path('direct/', include('direct.urls')),

    # SimpleJWT URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),
]
