from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin

from . import models


class UserAdmin(BaseAdmin):
    pass


admin.site.register(models.User, UserAdmin)
