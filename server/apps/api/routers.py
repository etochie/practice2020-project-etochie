from rest_framework import routers

from apps.core.viewsets import CafeViewSet, DishViewSet, IngredientViewSet
from apps.test.viewsets import TestViewSet
from apps.users.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('users', UserViewSet, basename='users')
router.register('cafe', CafeViewSet, basename='cafe')
router.register('dish', DishViewSet, basename='dish')
router.register('ingredient', IngredientViewSet, basename='ingredient')
