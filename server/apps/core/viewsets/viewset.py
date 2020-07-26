from rest_framework.viewsets import ModelViewSet

from apps.core.models import Cafe
from apps.core.serializers import CafeSerializer


class CafeViewSet(ModelViewSet):
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all()

    def perform_create(self, serializer):
        """Сохраняет владельца в serializer"""
        serializer.save(owner=self.request.user)