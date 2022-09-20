import logging

from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from mysite.authentication import CsrfExemptSessionAuthentication

logger = logging.getLogger(__name__)


class LoginAPIView(APIView):
    """
    Get log in status (GET), or log in (POST).
    """
    permission_classes = [AllowAny, ]
    authentication_classes = (CsrfExemptSessionAuthentication,)

    anon_result = {
        'userId': None,
        'username': '',
        'version': 0.1,
    }

    def get(self, request: Request):
        return Response({
            'userId': request.user.id,
            'username': request.user.username,
            'version': 0.1,
        }, status=status.HTTP_200_OK)

    def post(self, request: Request):
        username = request.data['username']
        password = request.data['password']

        logger.debug(f'Log in username: {username}, password: {password}')

        user = authenticate(username=username, password=password)  # User
        if user is not None:
            logger.debug(f'Log in: user authenticated.')

            login(request, user)

            result = {
                'userId': user.id,
                'username': user.username,
                'version': 0.1,
            }

            return Response(result)
        else:
            logger.debug(f'Log in: user authentication failed.')
            return Response(self.anon_result)
