from django.shortcuts import render
from rest_framework import generics, permissions

from core.admin import User


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.GenericAPIView):
    ...


class ReadUpdateUserView(generics.RetrieveUpdateAPIView):
    ...