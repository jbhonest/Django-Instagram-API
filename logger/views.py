from rest_framework import viewsets
from .models import PostView
from .serializers import PostViewSerializer


class LogPostView(viewsets.ModelViewSet):
    queryset = PostView.objects.all()
    serializer_class = PostViewSerializer
