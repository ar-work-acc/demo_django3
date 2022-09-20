from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Message(models.Model):
    """
    Chat messages.
    """
    from_user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.SET_NULL, null=True)
    to_user = models.ForeignKey(User, related_name='received_messages', on_delete=models.SET_NULL, null=True)
    text = models.TextField(default='', blank=True)
    created = models.DateTimeField(default=timezone.now)
