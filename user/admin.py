from django.contrib import admin
from user.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin  


class UserInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Users'

class CustomizedUserAdmin (UserAdmin):
    inlines = (UserInLine,)   

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

