from django.contrib import admin
from .models import SystemMessage

class SystemMessageAdmin(admin.ModelAdmin):
    list_display=("owner","content","link","status","create_timestamp","last_update_timestamp")

admin.site.register(SystemMessage,SystemMessageAdmin)
 