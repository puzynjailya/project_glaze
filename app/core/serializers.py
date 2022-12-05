from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.admin import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,
                                     write_only=True,
                                     style={'input_type': 'password', 'placeholder': 'Password'},
                                     )
    repeat_password = serializers.CharField(required=True,
                                            style={'input_type': 'password', 'placeholder': 'Password'},
                                            )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'password', 'repeat_password']

    def validate(self, data):
        if not data['password'] or not data['repeat_password']:
            raise ValidationError('Необходимо ввести оба поля')
        if data['password'] != data['repeat_password']:
            raise ValidationError('Введенные пароли не совпадают')
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(password=validated_data['password'])
        del validated_data['repeat_password']
        return super().create(validated_data)
