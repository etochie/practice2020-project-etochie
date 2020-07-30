from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from apps.core.models import Cafe, Dish, Ingredient
from apps.core.serializers import CafeSerializer, DishSerializer,\
    IngredientSerializer


class CafeViewSet(ModelViewSet):
    """ViewSet модели заведения"""
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all()

    def perform_create(self, serializer):
        """Сохраняет владельца в serializer"""
        serializer.save(owner=self.request.user)


class DishViewSet(ModelViewSet):
    """ViewSet модели блюда"""
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


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


class DishIngredientViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    """
    ViewSet фильтрации ингредиентов блюда
    Только GET запрос
    """
    serializer_class = IngredientSerializer

    def get_queryset(self):
        ingredients = Ingredient.objects.filter(dish=self.kwargs['pk'])
        return ingredients


class CafeDishesViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    """
    ViewSet фильтрации блюд заведения
    Только GET запрос
    """
    serializer_class = DishSerializer

    def get_queryset(self):
        dishes = Dish.objects.filter(cafe=self.kwargs['pk'])
        return dishes