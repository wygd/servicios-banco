# users/serializers.py
from rest_framework import serializers
from usuario import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('email', 'username','password','tipo_usuario')

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.Usuario(
            email = validated_data['email'],
            username = validated_data['username'],
            tipo_usuario = validated_data['tipo_usuario']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user