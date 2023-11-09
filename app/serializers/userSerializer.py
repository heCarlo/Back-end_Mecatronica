from rest_framework import serializers
from ..models.users import UserEntity

class UserEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntity
        fields = '__all__'
