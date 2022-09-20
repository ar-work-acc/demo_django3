import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class ChatApp(LoginRequiredMixin, TemplateView):
    """
    The page for our chat app. Requires the user to log in first.
    """
    login_url = '/admin/login/'
    template_name = 'chat/app.html'


# class ChatAppRoom(LoginRequiredMixin, TemplateView):
#     """
#     The page for our chat app room.
#     """
#     login_url = '/admin/login/'
#     template_name = 'chat/room.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ChatAppRoom, self).get_context_data(**kwargs)
#         room_name = kwargs.get('room_name', None)
#         logger.debug(f'chap app room name: {room_name}')
#         context['room_name'] = room_name
#
#         return context
