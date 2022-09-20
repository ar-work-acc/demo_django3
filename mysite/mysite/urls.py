"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from .views import LoginAPIView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # for the "Log in" to show up
    path('api/v1/', include([
        path('login/', LoginAPIView.as_view()),
        path('', include('chat.urls_api')),  # main chat app API
    ])),

    path('chat/', include('chat.urls_template')),

    # Django admin:
    path('admin/', admin.site.urls),
]

# These are for local development only:
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)