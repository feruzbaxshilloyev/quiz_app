from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_superuser')
    ordering = ('email',)
    search_fields = ('email', 'name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Shaxsiy maʼlumotlar', {'fields': ('name',)}),
        ('Ruxsatlar', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Tizim maʼlumotlari', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_superuser')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
