from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

from .models import Test

class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('name', 'telephone',  'admin',)
    list_filter = ('staff','active' ,'admin', )
    fieldsets = (
        (None, {'fields': ('telephone', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('telephone', 'password1', 'password2')}
        ),
    )

    search_fields = ('telephone','name')
    ordering = ('telephone','name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


admin.site.unregister(Group)
admin.site.register(Test)