from rest_framework import serializers
from django.contrib.auth.models import User
from app.models.users.userEntity import UserEntity

class UserEntitySerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    username_id = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserEntity
        fields = ['username', 'password', 'email', 'username_id']

    def create(self, validated_data):
        user_data = {
            'username': validated_data['username'],
            'password': validated_data['password'],
            'email': validated_data['email'],
        }
        user = User.objects.create_user(**user_data)
        user_entity = UserEntity.objects.create(user=user, email=validated_data['email'])
        
        return user_entity
