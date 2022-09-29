from django.contrib import admin
from .models import CustomUser  ,TokenActivation 
from django.contrib.auth.admin import UserAdmin


class CustomUserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'first_name',)
    list_filter = ('email', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdminConfig) 
admin.site.register(TokenActivation)
   