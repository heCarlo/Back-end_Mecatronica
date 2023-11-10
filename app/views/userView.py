from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from app.models.users.userEntity import UserEntity
from app.serializers.userSerializer import UserEntitySerializer

class UserEntityListView(generics.ListCreateAPIView):
    queryset = UserEntity.objects.all()
    serializer_class = UserEntitySerializer

class UserEntityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserEntity.objects.all()
    serializer_class = UserEntitySerializer