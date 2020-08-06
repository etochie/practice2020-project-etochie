from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """Проверяет, является ли пользователь владельцем заведения."""
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user


class DishEditOnlyOwner(BasePermission):
    """
    Проверяет, является ли пользователь владельцем заведения,
    к которому привязано блюдо.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.cafe:
            user_cafes = request.user.cafes.filter()
            return obj.cafe in user_cafes
        # если блюдо не привязано к заведению,
        # его могут редактировать все авторизированные пользователи
        else:
            return True
