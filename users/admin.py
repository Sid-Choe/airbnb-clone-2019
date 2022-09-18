from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms_model


class RoomInline(admin.TabularInline):

    model = rooms_model.Room

@admin.register(models.User)
class UserAdmin(UserAdmin):

    """ Custom User Admin """

    inlines = (RoomInline, )

    fieldsets = UserAdmin.fieldsets + \
        (("Custom Profile", {"fields": ("avatar", "gender",
         "bio", "language", "currency", "super_host")}),)
    
    list_filter = UserAdmin.list_filter + ("super_host",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_active",
        "super_host",
        "is_staff",
        "is_superuser",
    )
