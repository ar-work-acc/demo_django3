from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),  # for the "Log in" to show up
    path('', include(router.urls))

    # path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    #
    # path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    #
    # path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
