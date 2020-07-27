from rest_framework import serializers

from apps.core.models import Cafe


class CafeSerializer(serializers.ModelSerializer):
    """
    Serializer для модели Cafe
    Для выполнения условий задания в поле owner задаем source='owner.id'
    """
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Cafe
        fields = '__all__'
