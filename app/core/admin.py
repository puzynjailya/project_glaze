from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('user_name', 'email', 'phone')
    readonly_fields = ('last_login', 'date_joined')
