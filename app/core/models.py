from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Phone Number')
    user_image = models.ImageField(upload_to='user_images', null=True, blank=True, verbose_name='Userpic')
    is_deleted = models.BooleanField(default=False, verbose_name='status')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('phone', 'username', 'email')
