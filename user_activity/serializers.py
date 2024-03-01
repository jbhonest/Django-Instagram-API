from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'user', 'created_at')

    def get_fields(self):
        fields = super().get_fields()
        if 'user' in fields:
            # Make user field read_only in the browsable API
            fields['user'].read_only = True
        return fields
