from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('mobile_no', 'email', 'first_name', 'last_name')
    list_filter = ('mobile_no', 'email', 'name', 'is_active', 'is_staff')
    ordering = ('-joining_date',)
    list_display = ('email', 'mobile_no', 'name',
                    'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'is_email_verified', 'mobile_no',
         'is_mobile_no_verified', 'name', 'address', 'profile_pic')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_no', 'email', 'name', 'password1', 'password2', 'is_active', 'is_staff', 'user_permissions', 'groups', 'profile_pic')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
