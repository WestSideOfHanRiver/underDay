from django.contrib import admin
from .models import User

class UserItemAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(User, UserItemAdmin)