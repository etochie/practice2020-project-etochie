from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters import rest_framework as filters
from drf_yasg.inspectors import CoreAPICompatInspector, NotHandled
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.core.models import Cafe, Dish, Ingredient
from apps.core.serializers import CafeSerializer, DishSerializer, \
    IngredientSerializer
from apps.main.permissions import CafeIsAuthenticatedAndOwnerOrReadOnly, \
    DishIsAuthenticatedAndOwnerOrReadOnly


class DjangoFilterDescriptionInspector(CoreAPICompatInspector):
    """Добавляет описание к полям филтрации"""
    def get_filter_parameters(self, filter_backend):
        if isinstance(filter_backend, filters.DjangoFilterBackend):
            result = super(DjangoFilterDescriptionInspector, self).get_filter_parameters(filter_backend)
            for param in result:
                if not param.get('description', ''):
                    param.description = "Filter the returned list by {field_name}".format(field_name=param.name)

            return result

        return NotHandled


@method_decorator(name='list', decorator=swagger_auto_schema(
    filter_inspectors=[DjangoFilterDescriptionInspector]
))
@method_decorator(name='list', decorator=cache_page(timeout=60*15))
@method_decorator(name='retrieve', decorator=cache_page(timeout=60*15))
class CafeViewSet(ModelViewSet):
    """Cafe model ViewSet"""
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['dishes']
    permission_classes = [CafeIsAuthenticatedAndOwnerOrReadOnly]

    def perform_create(self, serializer):
        """Сохраняет владельца в serializer"""
        serializer.save(owner=self.request.user)


@method_decorator(name='list', decorator=swagger_auto_schema(
    filter_inspectors=[DjangoFilterDescriptionInspector]
))
class DishViewSet(ModelViewSet):
    """Dish model ViewSet"""
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['cafe']
    permission_classes = [DishIsAuthenticatedAndOwnerOrReadOnly]


@method_decorator(name='list', decorator=swagger_auto_schema(
    filter_inspectors=[DjangoFilterDescriptionInspector]
))
class IngredientViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    """
    Ingredient model ViewSet
    """
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['dish']
    permission_classes = [IsAuthenticatedOrReadOnly]
