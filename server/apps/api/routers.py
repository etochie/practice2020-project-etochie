from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets import UserViewSet
from apps.core.viewsets import CafeViewSet


router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('users', UserViewSet, basename='users')
router.register('cafe', CafeViewSet, basename='cafe')
