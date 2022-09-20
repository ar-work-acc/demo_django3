from django.urls import path

from .views.template import ChatApp

app_name = 'chat'

urlpatterns = [
    path('', ChatApp.as_view(), name='index'),
    # path('<str:room_name>/', ChatAppRoom.as_view(), name='room'),
]
