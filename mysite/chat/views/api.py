import json
import logging

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from chat.models import Message
from chat.serializers import ChatMessageSerializer, ChatUserSerializer

logger = logging.getLogger(__name__)
channel_layer = get_channel_layer()


class ChatUserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view set automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = ChatUserSerializer


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.none()
    serializer_class = ChatMessageSerializer

    # TODO permission classes

    def get_queryset(self):
        target_user_id = self.request.query_params.get('targetUserId', None)
        logger.debug(f'taget user ID: {target_user_id}')

        user = self.request.user  # type: User

        if not user.username:
            # "user" might be an AnonymousUser (not logged in)
            return self.queryset
        else:
            if target_user_id is None:
                queryset = Message.objects.filter(
                    Q(from_user=user) | Q(to_user=user),
                ).order_by('created')
            else:
                queryset = Message.objects.filter(
                    Q(from_user=user, to_user=target_user_id) | Q(to_user=user, from_user=target_user_id),
                ).order_by('created')
            return queryset

    def perform_create(self, serializer):
        """
        Send data to web socket (TODO should be moved to Model's save method instead?)
        """
        super(ChatMessageViewSet, self).perform_create(serializer)
        logger.debug(repr(serializer.data))
        async_to_sync(channel_layer.group_send)(f"{serializer.data['to_user']}",
                                                {
                                                    "type": "notify_user",
                                                    "id": serializer.data['id'],
                                                    "text": serializer.data['text'],
                                                    "from_user": serializer.data['from_user'],
                                                    "to_user": serializer.data['to_user'],
                                                    "created": serializer.data['created'],
                                                })
