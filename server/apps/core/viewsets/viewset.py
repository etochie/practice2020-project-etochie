from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from django_filters import rest_framework as filters

from apps.core.models import Cafe, Dish, Ingredient
from apps.core.serializers import CafeSerializer, DishSerializer,\
    IngredientSerializer


class CafeViewSet(ModelViewSet):
    """ViewSet модели заведения"""
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['dishes']

    def perform_create(self, serializer):
        """Сохраняет владельца в serializer"""
        serializer.save(owner=self.request.user)


class DishViewSet(ModelViewSet):
    """ViewSet модели блюда"""
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['cafe']


class IngredientViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    """
    ViewSet ингредиента
    Только GET запрос
    """
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['dish']
