from django.contrib import admin
from .models import UserPofile 
 
class UserPofileAdmin(admin.ModelAdmin):
    list_display=("user","sex","birthday")
     
 
admin.site.register(UserPofile,UserPofileAdmin)