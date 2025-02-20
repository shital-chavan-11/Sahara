from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'gender', 'is_ngo', 'otp_verified')
    list_filter = ('gender', 'is_ngo', 'otp_verified', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('contact_number', 'gender')}),
        ('OTP Verification', {'fields': ('otp_code', 'otp_verified')}),
        ('Permissions', {'fields': ('is_ngo', 'is_staff', 'is_active')}),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
