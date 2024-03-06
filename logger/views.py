from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from .models import PostView, ProfileView
from .serializers import PostViewSerializer, ProfileViewSerializer


class LogPostView(viewsets.ReadOnlyModelViewSet):
    queryset = PostView.objects.order_by('-pk')
    serializer_class = PostViewSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('post', 'viewer')


class LogProfileView(viewsets.ReadOnlyModelViewSet):
    queryset = ProfileView.objects.order_by('-pk')
    serializer_class = ProfileViewSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('profile', 'viewer')
