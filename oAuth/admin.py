from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from oAuth.models import NewUser


class NewUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'roles',)}),
        (_('Important dates'), {'fields': ('date_joined',)}),
    )

    list_display = ('id', 'username', 'roles', 'email', 'is_active', 'last_login')
    list_display_links = ('id', 'username', 'roles', 'email', 'last_login')
    search_fields = ('username', 'email')


admin.site.register(NewUser, NewUserAdmin)
