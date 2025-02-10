from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email' ,'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Usa create_user() que encripta la contraseña
        return user