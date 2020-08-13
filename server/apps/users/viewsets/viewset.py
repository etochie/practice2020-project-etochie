from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users.serializers import UserSerializer


@method_decorator(name='create', decorator=swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password'],
        properties={
            'username': openapi.Schema(
                title='Имя пользователя',
                type=openapi.TYPE_STRING
            ),
            'password': openapi.Schema(
                title='Пароль',
                type=openapi.TYPE_STRING
            )
        },
    ),
    responses={'201': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(
                title='Имя пользователя',
                type=openapi.TYPE_STRING
            ),
            'token': openapi.Schema(
                title='Токен',
                type=openapi.TYPE_STRING
            )
        }
    )}
))
class UserViewSet(
    mixins.CreateModelMixin,
    GenericViewSet
):
    """
    A viewset that provides `create` action
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
