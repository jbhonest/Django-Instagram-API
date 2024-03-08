from rest_framework import serializers
from user_panel.serializers import SimpleUserSerializer
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender_info = SimpleUserSerializer(source='sender', read_only=True)
    receiver_info = SimpleUserSerializer(source='receiver', read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'sender', 'sender_info', 'receiver', 'receiver_info', 'content', 'created_at',
                  )

    def get_fields(self):
        fields = super().get_fields()
        if 'sender' in fields:
            # Make sender field read_only in the browsable API
            fields['sender'].read_only = True
        return fields
