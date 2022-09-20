from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.api import ChatMessageViewSet, ChatUserViewSet

router = DefaultRouter()
router.register(r'users', ChatUserViewSet)
router.register(r'messages', ChatMessageViewSet)

# For APIs only:
urlpatterns = [
    path('', include(router.urls))
]
