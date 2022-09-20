from django.contrib.auth.models import User
from rest_framework import serializers

from chat.models import Message


class ChatUserSerializer(serializers.ModelSerializer):
    """
    For listing chat users (friends).
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'last_login', ]


class ChatMessageSerializer(serializers.ModelSerializer):
    """
    Chat messages
    """

    class Meta:
        model = Message
        fields = "__all__"
