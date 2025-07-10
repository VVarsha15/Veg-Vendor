from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Vegetable, CartItem, Order,OrderItem

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['phone', 'name', 'address', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser', 'is_active']

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal Info', {'fields': ('name', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'name', 'address', 'password1', 'password2'),
        }),
    )

    search_fields = ['phone']

    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Vegetable)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

