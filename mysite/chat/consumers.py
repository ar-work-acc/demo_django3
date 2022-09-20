import json
import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

logger = logging.getLogger(__name__)


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.group_name = None

    def connect(self):
        user = self.scope['user']
        self.group_name = f'{user.id}'
        logger.debug(
            f'current user ID: {user.id}, room name = {self.group_name}')

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()  # should be the last action in connect()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        pass
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        #
        # user = self.scope['user']
        #
        # # Send message to room group
        # async_to_sync(self.channel_layer.group_send)(
        #     self.group_name,
        #     {
        #         'type': 'chat_message',  # defines instance method name "chat_message"
        #         'message': f'{user.username} : {message}',
        #     }
        # )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    # send message to listener when a message is created for target user:
    def notify_user(self, event):
        user_id = event['id']
        text = event['text']
        from_user = event['from_user']
        to_user = event['to_user']
        created = event['created']
        logger.debug(f'Got text: {text} from user: {from_user}')

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'id': user_id,
            'message': text,
            'from': from_user,
            'to': to_user,
            'created': created,
        }))
