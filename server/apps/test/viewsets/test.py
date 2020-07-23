from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.test.models import Test
from apps.test.serializers import TestSerializer


class TestViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    """
    A viewset that provides `create`, `list` and `retrieve` actions
    """
    serializer_class = TestSerializer
    queryset = Test.objects.all()
