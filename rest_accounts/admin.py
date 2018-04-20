from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from rest_accounts.models import UserProfile


# Register your models here.
UserAdmin.list_display += (
    'phone',
)

UserAdmin.list_filter += (
    'phone',
)

UserAdmin.fieldsets[1][1]['fields'] += (
    'phone',
)

admin.site.register(UserProfile, UserAdmin)
