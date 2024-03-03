from django.contrib import admin
from django.contrib import admin
from app.models import UserAccount

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('Email', 'PhoneNumber', 'Nickname')


admin.site.register(UserAccount, UserAccountAdmin)