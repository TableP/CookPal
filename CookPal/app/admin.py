from django.contrib import admin
from django.contrib import admin
from app.models import UserAccount, Recipe, Support

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('Email', 'PhoneNumber', 'Nickname')

class recipeAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Ingredients', 'Instructions')

class supportAdmin(admin.ModelAdmin):
    list_display = ('Name', 'SupportID')



admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Recipe, recipeAdmin)
admin.site.register(Support, supportAdmin)