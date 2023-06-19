from django.contrib import admin
from .models import UrMaster


class UrMasterItemAdmin(admin.ModelAdmin):
    list_display = ('user_numb', 'user_phon', 'user_name', 'user_nick')


admin.site.register(UrMaster, UrMasterItemAdmin)
