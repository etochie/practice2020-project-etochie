from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User objects"""
    token = serializers.CharField(
        max_length=255, read_only=True, source='auth_token.key'
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        data = self.get_initial()
        data['token'] = Token.objects.create(user=user)
        user.refresh_from_db()
        return user


