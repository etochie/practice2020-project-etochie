from rest_framework import serializers

from apps.core.models import Cafe, Dish, Ingredient


class CafeSerializer(serializers.ModelSerializer):
    """
    Serializer для модели Cafe
    Для выполнения условий задания в поле owner задаем source='owner.id'
    """
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Cafe
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    """Serializer для модели блюда"""
    class Meta:
        model = Dish
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer для модели ингредиента"""
    class Meta:
        model = Ingredient
        fields = '__all__'