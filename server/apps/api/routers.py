from rest_framework import routers

from apps.core.viewsets import CafeViewSet, DishViewSet,\
    IngredientViewSet, DishIngredientViewSet, CafeDishesViewSet
from apps.test.viewsets import TestViewSet
from apps.users.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('users', UserViewSet, basename='users')
router.register('cafe', CafeViewSet, basename='cafe')
router.register('cafe/(?P<pk>[^/.]+)/dishes', CafeDishesViewSet,
                basename='cafe-dishes')
router.register('dish', DishViewSet, basename='dish')
router.register('dish/(?P<pk>[^/.]+)/ingredients', DishIngredientViewSet,
                basename='dish-ingredients')
router.register('ingredient', IngredientViewSet, basename='ingredient')
