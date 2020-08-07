from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    BasePermission, SAFE_METHODS


class CafeIsAuthenticatedAndOwnerOrReadOnly(IsAuthenticatedOrReadOnly):
    """Проверяет, является ли пользователь владельцем заведения"""

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user == obj.owner
        )


class DishIsAuthenticatedAndOwnerOrReadOnly(BasePermission):
    """
    Проверяет, является ли пользователь владельцем заведения,
    к которому привязано блюдо.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.cafes.filter(id=request.POST['cafe']).exists()
        )

    def has_object_permission(self, request, view, obj):
        dish_cafe = obj.cafe.id
        return bool(
            request.method in SAFE_METHODS or
            request.user.cafes.filter(id=dish_cafe).exists()
        )
