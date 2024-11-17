from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_active', 'is_staff')
    # Ensure 'phone_number' is listed here
    search_fields = ('username', 'email', 'phone_number')  # Optional: make phone_number searchable
    list_filter = ('is_active', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
