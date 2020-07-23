from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from django.contrib.auth.models import User
from apps.users.serializers import UserSerializer


class UserViewSet(
    mixins.CreateModelMixin,
    GenericViewSet
):
    """
    A viewset that provides `create` action
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
