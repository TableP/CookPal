from django.contrib import admin
from django.contrib import admin
from app.models import UserAccount, Recipe

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('Email', 'PhoneNumber', 'Nickname')

class recipeAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Ingredients', 'Instructions')


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Recipe, recipeAdmin)